# Section 1 — Hard: Annotate a data-processing module

**Goal:** Add type annotations to a small ETL-style module with nested containers, optional values, and a few gotchas.

## What to do

Open [`starter.py`](./starter.py). It parses a list of CSV-like rows into structured records and computes some aggregates. Annotate:

1. All top-level constants
2. All function signatures (params + returns)
3. Any local variable whose inferred type is not obvious from context
4. Any nested container (e.g. `list[dict[str, list[int]]]`)

Run:

```bash
pyrefly check sections/01-adding-annotations/exercises/hard/starter.py
```

## What you'll practise

- Deeply nested containers (`dict[str, list[Record]]`)
- Aliases via `type` statements (Python 3.12+) or `TypeAlias` for clarity
- `Optional`/`| None` for fields that may be missing
- Tuple types with fixed vs variable length (`tuple[str, int]` vs `tuple[int, ...]`)
- Typing generator/iterator return values (`Iterator[str]`)

## Bonus challenges

Once you have a clean typecheck:
- Introduce a `TypedDict` for the row-record shape and use it everywhere.
- Introduce a `dataclass` version of the record and see how the annotations shift.
- Turn one of the functions into a generator (`yield`) and annotate its return type.
