"""Live-demo starting point for Section 2.

A small "user cache" module. It works, but the types are loose: dict[str, Any]
everywhere, no notion of "the user might not exist", and hard-coded strings for
roles.

We'll tighten it step by step during the demo — focusing on unions, literals,
and a dataclass. Generics, protocols, and overloads have their own exercises.
See demo_final.py for the finished version.
"""

from typing import Any


_CACHE: dict[int, dict[str, Any]] = {}


def add_user(uid, name, role, metadata):
    _CACHE[uid] = {"id": uid, "name": name, "role": role, "metadata": metadata}


def get_user(uid):
    return _CACHE.get(uid)


def promote(uid):
    user = _CACHE.get(uid)
    if user is None:
        return
    if user["role"] == "member":
        user["role"] = "moderator"
    elif user["role"] == "moderator":
        user["role"] = "admin"


if __name__ == "__main__":
    add_user(1, "Abby", "member", "full access")
    add_user(2, "Conner", "moderator", False)
    promote(1)
    print(get_user(1))
