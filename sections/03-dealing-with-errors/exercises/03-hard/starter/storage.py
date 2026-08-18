"""Persistence — save/load a TaskStore to a JSON file."""

import json
from pathlib import Path

from .models import Priority, Task, TaskStore


def save(store: TaskStore, path: Path) -> None:
    payload = [
        {
            "id": t.id,
            "title": t.title,
            "priority": t.priority,
            "done": t.done,
            "tags": t.tags,
        }
        for t in store.all()
    ]
    # BUG: what type does Path.write_text expect?
    path.write_text(payload)


def load(path: Path) -> TaskStore:
    raw = path.read_text()
    data = json.loads(raw)
    store = TaskStore()
    for item in data:
        # BUG: item["priority"] is `str`, not the required Literal.
        # Fix by narrowing (assert / cast / runtime validation).
        priority: Priority = item["priority"]
        task = store.add(item["title"], priority=priority, tags=item["tags"])
        if item["done"]:
            store.complete(task.id)
    return store
