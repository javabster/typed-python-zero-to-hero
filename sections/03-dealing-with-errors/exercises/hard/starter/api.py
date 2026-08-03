"""Thin api layer between the store and the CLI."""

from .models import Priority, Task, TaskStore
from .filters import by_priority, by_tag


def add_task(store: TaskStore, title: str, priority: Priority = "medium") -> Task:
    return store.add(title=title, priority=priority)


def list_by_priority(store: TaskStore, priorities: list[Priority]) -> list[Task]:
    return by_priority(store.all(), priorities)


def list_by_tag(store: TaskStore, tag: str) -> list[Task]:
    return by_tag(store.all(), tag)


def summary_lines(tasks: list[Task]) -> list[str]:
    # BUG: t.summary is a bound method — .upper() doesn't exist on it.
    return [f"{t.id}. {t.summary.upper()}" for t in tasks]


def mark_done(store: TaskStore, task_id: int) -> None:
    store.complete(task_id)
