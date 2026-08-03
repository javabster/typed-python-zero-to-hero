# Section 2 — Easy: Unions and Optionals

**Goal:** Introduce `X | None` and `X | Y` types into a small helper module. Get comfortable expressing "either/or" and "maybe missing" in signatures.

## What to do

Open [`starter.py`](./starter.py). Each function has a docstring describing what it accepts and returns. Add annotations that faithfully capture those descriptions, including:

- functions that accept **either** an `int` **or** a `str`
- functions that **may return `None`**
- a config loader that returns different shapes for different keys

Run:

```bash
pyrefly check sections/02-advanced-typing/exercises/easy/starter.py
```

## What you'll practise

- `X | None` for optional returns
- `X | Y` for "either/or" parameters
- Narrowing with `isinstance` inside a function body
- Using `assert x is not None` to satisfy the checker after an existence check

## Hints

- When a parameter is `int | str`, you'll typically need to `isinstance`-check before you can call type-specific methods on it.
- `dict[str, int | str | bool]` is a valid (if loose) way to type a heterogeneous config dict — but see if you can do better on the parts you know.
