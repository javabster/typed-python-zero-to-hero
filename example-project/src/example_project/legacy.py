"""Legacy module — messy older code we're not ready to fix today.

The Section 4 exercise configures pyrefly to warn (not error) on issues
from this module, so they stay visible without failing CI.

Each bug below is a real runtime bug that pyrefly catches — no incorrect
annotations.
"""


class URLBag:
    """Bag of URLs. Has a few subtle bugs — legacy code, we know."""

    def __init__(self) -> None:
        # items starts as None and gets initialised on first add(). Classic
        # lazy-init pattern that becomes a foot-gun once we add types.
        self.items: list[str] | None = None

    def add(self, x: str) -> None:
        # BUG: at runtime, the first call to add() crashes:
        # AttributeError: 'NoneType' object has no attribute 'append'.
        self.items.append(x)

    def first(self) -> str:
        # BUG: even after items is a list, this can crash when empty
        # (IndexError) — but pyrefly catches the more urgent one:
        # calling [0] on possibly-None.
        return self.items[0]


def normalise(url: str | None) -> str:
    # BUG: normalise(None) would crash at runtime:
    # AttributeError: 'NoneType' object has no attribute 'strip'.
    return url.strip().rstrip("/")


def domain_of(url: str) -> str:
    parts = url.split("://")
    # BUG: `.upper` (no parens) returns the bound METHOD, not the uppercased
    # string. The function is annotated `-> str` — pyrefly catches the mismatch.
    # If this ran, callers would get something like `<built-in method upper of str object>`.
    return parts[1].split("/")[0].upper
