# Section 3 — Intermediate: Subtler type errors

**Goal:** Fix errors where the *code* is fine at runtime but the typechecker is (correctly!) unhappy. These are the kinds of errors most people get stuck on.

## What to do

Run pyrefly:

```bash
pyrefly check sections/03-dealing-with-errors/exercises/02-intermediate/starter.py
```

Pyrefly reports **3 errors**, one for each of these:

1. **Variance** (BUG B) — you can't pass a `list[Dog]` where `list[Animal]` is expected, because the function appends to it
2. **Narrowing failures** (BUG C) — pyrefly can't tell you've already checked for `None` in a different function
3. **Missing return in some branches** (BUG D) — a function annotated `-> int` that only returns on some paths

There is also a **fourth bug that pyrefly does not report**:

4. **Mutable default arguments** (BUG A) — the classic `def f(items=[])` foot-gun

BUG A is deliberate. Annotating a function completely does not make it correct, and a typechecker doesn't always do the work of a linter: pyrefly's job is type mismatches, and a shared-by-every-call default list isn't one. Fix it too — just don't expect the error count to move. (Tools like ruff's `B006` rule catch this; type checking and linting complement each other.)

Fix all four. Some fixes will be "restructure the code", others "fix the caller rather than the signature", others "guard with `assert`". Try to pick the *narrowest* fix each time.

## What you'll practise

- Type narrowing with `isinstance`, `is not None`, `assert`
- The `Sequence[T]` / `Iterable[T]` covariant escape hatch
- Why invariance exists, and when the right fix is the caller rather than the signature
- Recognising the limits of a typechecker — what it will and won't catch for you
- Reading `[error-code]` labels and using them to look up docs

## Rules

- No changing an annotation to a broader type than needed just to hide an error (`Any`/`object`). Fix the code, or use a more appropriate container (`Sequence`).
- **No `# pyrefly: ignore` in this file.** All three errors have a real fix. If you're reaching for a suppression, you're papering over a bug for this exercise. There are valid use cases of ignores though (such as type checker bugs or difficult-to-express functionality).

Ask an instructor if you'd like to see a reference solution.
