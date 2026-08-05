"""Domain model. Fully typed — most of this is correct."""

from .hashing import short_code


class ShortLink:
    def __init__(self, target: str, code: str | None = None) -> None:
        self.target: str = target
        self.code: str = code or short_code(target)
        self.hits: int = 0

    def visit(self) -> str:
        self.hits += 1
        return self.target


class LinkStore:
    def __init__(self) -> None:
        self._by_code: dict[str, ShortLink] = {}

    def shorten(self, url: str) -> ShortLink:
        link = ShortLink(url)
        self._by_code[link.code] = link
        return link

    def resolve(self, code: str) -> ShortLink | None:
        return self._by_code.get(code)

    def all_codes(self) -> list[str]:
        return list(self._by_code.keys())

    def describe(self, code: str) -> str:
        """Return a one-line summary of the link with this code."""
        link = self.resolve(code)
        # REAL BUG: forgot the None check. At runtime, calling describe() with
        # an unknown code crashes: AttributeError: 'NoneType' has no 'target'.
        return f"{link.target} ({link.hits} hits)"
