# Section 2: Advanced Typing Features

**Time:** 45 min (15 min demo + 30 min exercises)

## What you'll learn

- **Unions** (`X | Y`) and `Optional` — expressing "either/or" and "maybe missing"
- **Generics** with `TypeVar` and the PEP 695 `[T]` syntax
- **Protocols** — structural typing / "duck typing that the typechecker understands"
- **Literals** — narrowing string/int types to specific values
- **Custom types** — `NewType`, `TypeAlias`, `type X = ...`

## Demo

We'll walk through [`demo/demo.py`](./demo/demo.py) — a small refactor that starts with `dict[str, Any]` everywhere and progressively tightens the types using each of the features above.

Key talking points:
1. `Union` and `Optional` from `typing` still work, but `X | Y` and `X | None` (PEP 604) are the modern preferred forms.
2. `TypeVar` lets a function/class say "the type doesn't matter — but the *same* type appears in multiple places."
3. `Protocol` lets you type-check against a structural shape (methods/attributes) rather than a nominal class. This is how you type things like "any object with a `.read()` method".
4. `Literal["red", "green", "blue"]` gives you enum-like safety with plain strings.
5. Python 3.12's `type Foo = ...` and `class Container[T]:` remove a lot of boilerplate.

## Exercises

| Level          | Topic                                                          |
|----------------|----------------------------------------------------------------|
| [easy](./exercises/01-easy/)                 | Introduce `X | None` and `Union` into an untyped helper module |
| [intermediate](./exercises/02-intermediate/) | Rewrite a duplicated container class as a generic              |
| [hard](./exercises/03-hard/)                 | Define a `Protocol` for a plugin registry and pin state values with `Literal`  |

## Cheat sheet

```python
from typing import Literal, NewType, Protocol, TypeVar

# --- Unions ---
def find(name: str) -> User | None: ...
def load(source: str | Path | bytes) -> Config: ...

# --- Generics: pre-3.12 syntax ---
T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

# --- Generics: 3.12+ syntax ---
def first[T](items: list[T]) -> T:
    return items[0]

class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    def push(self, item: T) -> None: self._items.append(item)
    def pop(self) -> T: return self._items.pop()

# --- Protocols ---
class Readable(Protocol):
    def read(self, n: int = -1) -> bytes: ...

def load_bytes(source: Readable) -> bytes:
    return source.read()

# --- Literals ---
Colour = Literal["red", "green", "blue"]
def paint(colour: Colour) -> None: ...
paint("red")     # OK
paint("purple")  # type error

# --- NewType ---
UserId = NewType("UserId", int)
def fetch_user(uid: UserId) -> User: ...
```
