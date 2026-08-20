# Section 1 — Intermediate: Annotate a class

**Goal:** Add type annotations to the attributes and methods of a small class hierarchy.

## What to do

Open [`starter.py`](./starter.py). Annotate:
1. Every instance attribute (either at the class-body level or in `__init__`)
2. Every method's parameters and return value
3. Any local variables where the inferred type would be surprising

Then run:

```bash
pyrefly check sections/01-adding-annotations/exercises/02-intermediate/starter.py
```

## What you'll practise

- Class attribute annotations
- `__init__ -> None`
- Container attributes: `list[str]`, `dict[str, int]`
- Methods that take/return the class itself (`"Playlist"` string form or `from __future__ import annotations`)
- Optional attributes that start out as `None`
- `Callable[[Arg], Return]` for typing functions

## Hints

- Class attribute annotations can go directly under the `class` line, before `__init__`:
  ```python
  class Foo:
      name: str
      def __init__(self, name: str) -> None:
          self.name = name
  ```
- `__init__` always returns `None`. Yes, always. Even though it "returns" `self` conceptually.
- If a method returns "another instance of me", you can use `"ClassName"` as a forward reference — or `from __future__ import annotations` and use the bare name.
- For `filtered`, import `Callable` from `collections.abc`. The syntax is `Callable[[ArgType1, ArgType2, ...], ReturnType]`.
