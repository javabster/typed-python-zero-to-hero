# Section 2 — Intermediate: Make it generic

**Goal:** Rewrite a duplicated container class as a single generic class using `TypeVar` (or the PEP 695 `[T]` syntax if you're on Python 3.12+).

## What to do

Open [`starter.py`](./starter.py). You'll find `IntCache` and `StrCache` — two implementations of the same LRU-ish cache, one for ints and one for strs. Replace them with a single generic `Cache[T]` that behaves the same but works for any type.

Then update the demo at the bottom to use the new generic class.

Run:

```bash
pyrefly check sections/02-advanced-typing/exercises/02-intermediate/starter.py
```

## What you'll practise

- `TypeVar` (or PEP 695 `class Cache[T]:` syntax)
- Where the type parameter goes in a class body and method signatures
- Reasoning about "the same T flows through here" vs "these are different types"
- Bounded typevars (`TypeVar("T", bound=Comparable)`) — bonus challenge

## Hints

- Two valid ways to write the class header:
  ```python
  # Pre-3.12
  from typing import Generic, TypeVar
  T = TypeVar("T")
  class Cache(Generic[T]):
      def get(self, key: str) -> T | None: ...

  # 3.12+
  class Cache[T]:
      def get(self, key: str) -> T | None: ...
  ```
- The instance methods reference `T` — the class body variables should too.
- When you instantiate: `cache: Cache[int] = Cache()` or `Cache[int]()`.

## Bonus

Add a `max_value` parameter to the constructor and constrain `T` to be `Comparable` (something that supports `<` and `>`). Hint: define a `Protocol` for it. This is a stepping stone to Section 2 Hard.
