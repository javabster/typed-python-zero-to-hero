# Section 1 — Easy: Annotate simple functions

**Goal:** Add type annotations to a small collection of standalone functions.

## What to do

Open [`starter.py`](./starter.py). Every function is untyped. Add parameter and return-type annotations to each one so that `pyrefly check` runs clean.

```bash
pyrefly check sections/01-adding-annotations/exercises/easy/starter.py
```

## What you'll practise

- Primitive types: `int`, `str`, `float`, `bool`, `bytes`
- `None` return types (functions that print or mutate but don't return anything)
- Simple containers: `list[int]`, `dict[str, str]`, `tuple[int, int]`
- Optional parameters with default values

## Hints

- If a parameter has a default value, its type usually matches the default. E.g. `def f(x=0)` → `def f(x: int = 0)`.
- A function that only calls `print` (no `return`) returns `None`.
- `x | None` means "an X or None".

If you'd like to see a reference solution, ask an instructor — but try it yourself first!
