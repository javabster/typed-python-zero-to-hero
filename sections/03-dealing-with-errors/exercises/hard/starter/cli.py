"""Toy CLI dispatch — take a command name and arguments, do the thing."""

from .api import add_task, list_by_priority, list_by_tag, mark_done, summary_lines
from .models import TaskStore


def dispatch(store: TaskStore, command: str, *args: str) -> list[str]:
    if command == "add":
        title = args[0]
        # BUG: passing str with no validation as a Priority.
        priority = args[1] if len(args) > 1 else "medium"
        task = add_task(store, title, priority)
        return [f"Added task {task.id}"]

    if command == "done":
        # BUG: args[0] is str, mark_done wants int.
        mark_done(store, args[0])
        return [f"Marked {args[0]} done"]

    if command == "list":
        return summary_lines(store.all())

    if command == "by-tag":
        return summary_lines(list_by_tag(store, args[0]))

    if command == "by-priority":
        priorities = list(args)
        return summary_lines(list_by_priority(store, priorities))

    return [f"Unknown command: {command}"]
