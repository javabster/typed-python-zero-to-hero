"""EXTRA-HARD — overloads (Part A) and ParamSpec decorator factories (Part B).

Two independent tasks. Do Part A first, then Part B if you have time.
"""

from typing import Any


# ---------------------------------------------------------------------------
# PART A — @overload
#
# `fetch` returns a different concrete type depending on the `format` argument:
#
#   fetch(url, format="json")  -> dict[str, Any]
#   fetch(url, format="text")  -> str
#   fetch(url, format="bytes") -> bytes
#
# Right now callers get `dict[str, Any] | str | bytes` back and have to
# isinstance-check every time. Add @overload declarations so pyrefly can pick
# the exact return type from the `format` literal.
#
# Requirements:
#   1. Add three @overload stubs above the implementation, one per format.
#   2. Use `Literal["json"]`, `Literal["text"]`, `Literal["bytes"]` on the
#      format parameter of each stub.
#   3. Keep the implementation function exactly as it is — its signature stays
#      as the fallback for anything the overloads don't cover.
#   4. Do NOT put @overload on the implementation. It goes on the stubs only.
#
# Verify by uncommenting the reveal_type() calls at the bottom — pyrefly
# should report the specific type, not the union.
# ---------------------------------------------------------------------------


def fetch(url: str, format: str = "json") -> dict[str, Any] | str | bytes:
    # Pretend this hits the network.
    raw = b'{"status": "ok"}'
    if format == "json":
        import json
        return json.loads(raw)
    if format == "text":
        return raw.decode("utf-8")
    if format == "bytes":
        return raw
    raise ValueError(f"unknown format: {format}")


# ---------------------------------------------------------------------------
# PART B — ParamSpec decorator factory
#
# `retry` is a decorator factory: `@retry(times=3)` wraps a function so it's
# re-called on failure. Right now the wrapper is typed with `Any` everywhere,
# so pyrefly loses the wrapped function's signature entirely:
#
#     @retry(times=3)
#     def fetch_score(user_id: int) -> float: ...
#
#     fetch_score("nope")   # <- this is a complicated signature for a type checker to infer, so pyrefly reports `Unknown`
#
# Rewrite the annotations using `ParamSpec` and `TypeVar` (or PEP 695 syntax)
# so that:
#   - The wrapped function keeps its original parameter types and return type.
#   - Calling `fetch_score("nope")` is a type error.
#   - Calling `fetch_score(42)` is fine and reveals type `float`.
#
# Hints:
#   - `from typing import ParamSpec, TypeVar`  (or PEP 695: `def retry[**P, R]`)
#   - `P` (ParamSpec) captures "all the params" — use it as `*args: P.args,
#     **kwargs: P.kwargs`.
#   - The return type of `decorator` is `Callable[P, R]`.
#   - You may need `Callable` from `collections.abc`.
# ---------------------------------------------------------------------------


def retry(times: int):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            last_exc: Exception | None = None
            for _ in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
            assert last_exc is not None
            raise last_exc
        return wrapper
    return decorator


@retry(times=3)
def fetch_score(user_id: int) -> float:
    return user_id * 1.5


if __name__ == "__main__":
    # --- Part A checks ---
    payload = fetch("https://example.com", format="json")
    # reveal_type(payload)       # should be dict[str, Any] once overloads land
    # reveal_type(fetch("u", format="text"))   # should be str
    # reveal_type(fetch("u", format="bytes"))  # should be bytes

    # --- Part B checks ---
    print(fetch_score(42))
    # fetch_score("nope")        # should be a type error once ParamSpec lands
