"""Live-demo starting point for Section 2.

A small "user cache" module. It works, but the types are loose: dict[str, Any]
everywhere, no way to distinguish user IDs from other ints, no notion of "the
user might not exist", and hard-coded strings for roles.

We'll tighten it step by step during the demo, using every feature the section
covers. See demo_final.py for the finished version.
"""

from typing import Any


_CACHE: dict[int, dict[str, Any]] = {}


def add_user(uid, name, role):
    _CACHE[uid] = {"id": uid, "name": name, "role": role}


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


def first(items):
    return items[0] if items else None


if __name__ == "__main__":
    add_user(1, "Abby", "member")
    add_user(2, "Conner", "moderator")
    promote(1)
    print(get_user(1))
    print(first([get_user(1), get_user(2)]))
