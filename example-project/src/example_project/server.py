"""Toy wsgiref-based server so we have no third-party deps.

Intentionally not annotated. Feel free to type this file up as a bonus after
finishing the intermediate config exercise.
"""

from wsgiref.simple_server import make_server

from .models import LinkStore

_STORE = LinkStore()


def app(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

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
        if link is None:
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"unknown code"]
        target = link.visit()
        start_response("302 Found", [("Location", target)])
        return [b""]

    start_response("400 Bad Request", [("Content-Type", "text/plain")])
    return [b"POST / with a URL body, or GET /<code>"]


def main():
    with make_server("", 8000, app) as httpd:
        print("Listening on :8000")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
