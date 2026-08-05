# Section 3: Dealing With Type Errors

**Time:** 45 min (15 min demo + 30 min exercises)

## What you'll learn

- What Pyrefly is and what a typechecker actually *does*
- How to run `pyrefly check` on a file, directory, or whole project
- How to read a Pyrefly error message and locate the root cause
- Common categories of type errors and their fixes:
  - "argument of type X isn't assignable to parameter of type Y"
  - "no attribute"
  - "possibly unbound" / narrowing failures
  - "return type doesn't match"
  - variance errors (`list[Animal]` vs `list[Dog]`)
- When to reach for `# type: ignore`, `cast()`, or `assert isinstance(...)` — and when to fix the underlying types instead

## Demo

We'll walk through [`demo/demo.py`](./demo/demo.py) live. It contains a small module with several planted type errors. We'll:

1. Run `pyrefly check demo/demo.py` and read the raw output
2. Diagnose each error in turn
3. Show three fix strategies: **fixing the types**, **narrowing with `isinstance`/`assert`**, and (as a last resort) **`# type: ignore[error-code]`**

See [`demo/demo_fixed.py`](./demo/demo_fixed.py) for the clean end state.

### Talking points

- Errors don't cascade the way runtime tracebacks do — read from the top and fix one at a time. Later errors may vanish once the earlier ones are resolved.
- The **error code** in `[brackets]` (e.g. `[not-assignable]`) is stable — you can Google it, ignore it specifically, or configure severity per-code.
- `# type: ignore` is a tool, not a defeat. But always use a specific error code so it stays narrow: `# pyrefly: ignore[not-assignable]`.
- `cast(T, x)` tells the checker "trust me, this is a T" — no runtime effect. Use sparingly.

## Exercises

| Level          | Topic                                                              |
|----------------|--------------------------------------------------------------------|
| [easy](./exercises/01-easy/)                 | Single file, ~5 errors, obvious fixes                              |
| [intermediate](./exercises/02-intermediate/) | Subtler errors: narrowing failures, variance, mutable defaults     |
| [hard](./exercises/03-hard/)                 | Multi-file mini-project — cross-module type errors to hunt down    |

## Reading a pyrefly error

```
sections/03-dealing-with-errors/demo/demo.py:14:5: error: `str` is not assignable to `int` [not-assignable]
   |
14 |     count = "three"
   |     ^^^^^
```

- **File:line:col** — where the error is
- **Message** — what pyrefly thinks is wrong
- **[error-code]** — the stable, ignorable code
- **Snippet** — usually the offending expression

## Cheat sheet: fix strategies

| Symptom                                              | First thing to try                                        |
|------------------------------------------------------|-----------------------------------------------------------|
| "`X \| None` isn't assignable to `X`"                | Guard: `if x is not None: ...` or `assert x is not None`  |
| "`str` isn't assignable to `int`"                    | Fix the source, or `int(x)` conversion                    |
| "Object of type `X` has no attribute `y`"            | Wrong type inferred — annotate the variable               |
| "Incompatible return type"                           | Fix the annotation, or fix the returned expression        |
| "Argument … isn't assignable to `list[Base]`"        | Variance — annotate as `Sequence[Base]` for read-only     |
| Something is genuinely a type-system limitation      | `cast(T, x)` or `# pyrefly: ignore[error-code]`           |
