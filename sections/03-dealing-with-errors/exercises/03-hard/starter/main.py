"""A scripted scenario — this is what should still work after your fixes."""

from .cli import dispatch
from .models import TaskStore


def run() -> None:
    store = TaskStore()
    for line in dispatch(store, "add", "Write slides", "high"):
        print(line)
    for line in dispatch(store, "add", "Book flight", "medium"):
        print(line)
    for line in dispatch(store, "add", "Buy milk"):
        print(line)
    for line in dispatch(store, "done", "1"):
        print(line)
    print("--- all ---")
    for line in dispatch(store, "list"):
        print(line)


if __name__ == "__main__":
    run()
