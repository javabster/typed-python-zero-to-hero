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
        # NOT an error, which is expected. `json.loads` returns `Any`,
        # so `item["priority"]` is `Any`, and `Any` silently satisfies every
        # annotation, including `Priority`. Pyrefly reports nothing here.
        #
        # The code is still wrong: a hand-edited JSON file can put "urgent"
        # into this variable and nothing will stop it until something
        # downstream breaks. Typed code is only as trustworthy as its
        # untyped boundaries. Validate at runtime where `Any` gets in.
        priority: Priority = item["priority"]
        task = store.add(item["title"], priority=priority, tags=item["tags"])
        if item["done"]:
            store.complete(task.id)
    return store
