"""Toy wsgiref-based server so we have no third-party deps.

Fully typed — but the request handling has a couple of real bugs.
"""

from collections.abc import Callable, Iterable
from typing import Any
from wsgiref.simple_server import make_server

from .models import LinkStore

_STORE = LinkStore()

WsgiEnviron = dict[str, Any]
StartResponse = Callable[[str, list[tuple[str, str]]], Any]


def app(environ: WsgiEnviron, start_response: StartResponse) -> Iterable[bytes]:
    method: str = environ["REQUEST_METHOD"]
    path: str = environ["PATH_INFO"]

    if method == "POST" and path == "/":
        size = int(environ.get("CONTENT_LENGTH") or 0)
        url = environ["wsgi.input"].read(size).decode()
        link = _STORE.shorten(url)
        body = link.code.encode()
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [body]

    if method == "GET" and len(path) > 1:
        code = path[1:]
        link = _STORE.resolve(code)
        # REAL BUG: forgot the None check before calling .visit(). At runtime,
        # a GET for an unknown code crashes: AttributeError: 'NoneType' has no 'visit'.
        target = link.visit()
        start_response("302 Found", [("Location", target)])
        return [b""]

    start_response("400 Bad Request", [("Content-Type", "text/plain")])
    return [b"POST / with a URL body, or GET /<code>"]


def main() -> None:
    with make_server("", 8000, app) as httpd:
        print("Listening on :8000")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
