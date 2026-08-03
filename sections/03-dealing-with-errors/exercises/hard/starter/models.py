"""Domain models — tasks and priorities.

Several planted type errors in here. Fixing this file first is the right call —
most of the errors in the other files are downstream of these.
"""

from dataclasses import dataclass, field
from typing import Literal

Priority = Literal["low", "medium", "high"]


@dataclass
class Task:
    id: int
    title: str
    priority: Priority
    done: bool = False
    tags: list[str] = field(default_factory=list)

    def summary(self) -> str:
        marker = "x" if self.done else " "
        return f"[{marker}] ({self.priority}) {self.title}"


class TaskStore:
    def __init__(self) -> None:
        # BUG: should be dict[int, Task] — but is annotated as list[Task] and used as a dict.
        self._tasks: list[Task] = {}
        self._next_id: int = 1

    def add(self, title: str, priority: Priority = "medium", tags: list[str] | None = None) -> Task:
        task = Task(id=self._next_id, title=title, priority=priority, tags=tags or [])
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        # BUG: dict.get returns Task | None but signature says Task.
        return self._tasks.get(task_id)

    def complete(self, task_id: int) -> None:
        task = self.get(task_id)
        task.done = True   # cascading from the bug above

    def all(self) -> list[Task]:
        return list(self._tasks.values())
