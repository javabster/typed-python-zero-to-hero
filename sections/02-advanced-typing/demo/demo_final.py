"""Live-demo end state — demo.py after applying every technique in Section 2."""

from dataclasses import dataclass
from typing import Literal, NewType


UserId = NewType("UserId", int)
Role = Literal["member", "moderator", "admin"]


@dataclass
class User:
    id: UserId
    name: str
    role: Role


_CACHE: dict[UserId, User] = {}


def add_user(uid: UserId, name: str, role: Role) -> None:
    _CACHE[uid] = User(id=uid, name=name, role=role)


def get_user(uid: UserId) -> User | None:
    return _CACHE.get(uid)


def promote(uid: UserId) -> None:
    user = _CACHE.get(uid)
    if user is None:
        return
    if user.role == "member":
        user.role = "moderator"
    elif user.role == "moderator":
        user.role = "admin"


def first[T](items: list[T]) -> T | None:
    return items[0] if items else None


if __name__ == "__main__":
    add_user(UserId(1), "Abby", "member")
    add_user(UserId(2), "Conner", "moderator")
    promote(UserId(1))
    print(get_user(UserId(1)))
    print(first([get_user(UserId(1)), get_user(UserId(2))]))
