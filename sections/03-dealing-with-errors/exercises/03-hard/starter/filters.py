"""Filtering helpers — mostly clean, but with one genuinely tricky variance issue."""

from collections.abc import Callable

from .models import Task


def by_priority(tasks: list[Task], priorities: list[str]) -> list[Task]:
    # BUG (subtle): priorities is annotated list[str], but callers pass a
    # list[Literal["low","medium","high"]]. list[str] and
    # list[Literal[...]] aren't compatible in either direction — list is invariant.
    # Fix by widening the container type appropriately.
    return [t for t in tasks if t.priority in priorities]


def by_tag(tasks: list[Task], tag: str) -> list[Task]:
    return [t for t in tasks if tag in t.tags]


def matching(tasks: list[Task], predicate: Callable[[Task], bool]) -> list[Task]:
    return [t for t in tasks if predicate(t)]
