"""Legacy module. Represents older code we're not ready to fix yet.

Section 4 Intermediate exercise: configure pyrefly to warn (not error) on
issues from this module.

Do NOT annotate this file — the whole point is that it has messy types.
"""


class URLBag:
    def __init__(self):
        self.things = None

    def add(self, x):
        if self.things is None:
            self.things = []
        # deliberate type sloppiness — sometimes we get a str, sometimes a tuple.
        if isinstance(x, tuple):
            self.things.append(x[0])
        else:
            self.things.append(x)

    def first(self):
        # returns None if empty, otherwise the first element
        return self.things[0] if self.things else None


def normalise(url):
    return url.strip().rstrip("/")
