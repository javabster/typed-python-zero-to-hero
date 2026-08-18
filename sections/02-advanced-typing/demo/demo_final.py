"""Live-demo end state — demo.py after applying the techniques covered live.

Focus: unions, literals, dataclass. Generics/protocols/overloads/ParamSpec
have dedicated exercises.
"""

from dataclasses import dataclass
from typing import Literal


type Role = Literal["member", "moderator", "admin"]


@dataclass
class User:
    id: int
    name: str
    role: Role
    metadata: str | bool


_CACHE: dict[int, User] = {}


def add_user(uid: int, name: str, role: Role, metadata: str | bool) -> None:
    _CACHE[uid] = User(id=uid, name=name, role=role, metadata=metadata)


def get_user(uid: int) -> User | None:
    return _CACHE.get(uid)


def promote(uid: int) -> None:
    user = _CACHE.get(uid)
    if user is None:
        return
    if user.role == "member":
        user.role = "moderator"
    elif user.role == "moderator":
        user.role = "admin"


if __name__ == "__main__":
    add_user(1, "Abby", "member", "full access")
    add_user(2, "Conner", "moderator", False)
    promote(1)
    print(get_user(1))
