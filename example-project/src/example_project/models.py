"""Domain model. Intentionally not annotated."""

from .hashing import short_code


class ShortLink:
    def __init__(self, target, code=None):
        self.target = target
        self.code = code or short_code(target)
        self.hits = 0

    def visit(self):
        self.hits += 1
        return self.target


class LinkStore:
    def __init__(self):
        self._by_code = {}

    def shorten(self, url):
        link = ShortLink(url)
        self._by_code[link.code] = link
        return link

    def resolve(self, code):
        return self._by_code.get(code)

    def all_codes(self):
        return list(self._by_code.keys())
