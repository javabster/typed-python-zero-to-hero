# Section 1: Adding Type Annotations

**Time:** 45 min (15 min demo + 30 min exercises)

## What you'll learn

- The syntax for annotating variables, function parameters, and return values
- Common built-in types: `int`, `str`, `float`, `bool`, `bytes`, `None`
- Container types: `list[T]`, `dict[K, V]`, `tuple`, `set[T]`
- Annotating class attributes and methods
- When you can (and should) let Python infer types

## Demo

We'll walk through [`demo/demo.py`](./demo/demo.py) — a small untyped script — and add annotations to it live. See [`demo/demo_annotated.py`](./demo/demo_annotated.py) for the "after" version.

Key talking points:
1. Type annotations are **optional and don't affect runtime behavior** — they're for humans and tools.
2. Modern Python (3.9+) uses lowercase built-ins (`list[str]`) instead of `List[str]` from `typing`. We prefer the new syntax throughout this workshop.
3. Use `X | Y` (PEP 604) instead of `Union[X, Y]`, and `X | None` instead of `Optional[X]`.

## Exercises

Pick a difficulty level:

| Level          | Topic                                                                          |
|----------------|--------------------------------------------------------------------------------|
| [easy](./exercises/01-easy/)                 | Annotate simple functions with primitive types                     |
| [intermediate](./exercises/02-intermediate/) | Annotate a class with methods that use containers                  |
| [hard](./exercises/03-hard/)                 | Annotate a small data processing module with nested containers     |

Each exercise folder has its own `README.md` and a `starter.py` to edit. If you'd like to see a reference solution, ask an instructor.

## Cheat sheet

```python
# Variables
name: str = "Abby"
count: int = 3
prices: list[float] = [1.99, 2.50]
tags: dict[str, int] = {"python": 1}

# Functions
def greet(name: str) -> str:
    return f"Hello, {name}"

def maybe_double(x: int | None) -> int | None:
    return x * 2 if x is not None else None

# Classes
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
```
