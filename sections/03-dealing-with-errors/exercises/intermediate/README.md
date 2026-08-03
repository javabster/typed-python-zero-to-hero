# Section 3 — Intermediate: Subtler type errors

**Goal:** Fix errors where the *code* is fine at runtime but the typechecker is (correctly!) unhappy. These are the kinds of errors most people get stuck on.

## What to do

Run pyrefly:

```bash
pyrefly check sections/03-dealing-with-errors/exercises/intermediate/starter.py
```

There are several classes of error in this file:

1. **Narrowing failures** — pyrefly can't tell you've already checked for `None`
2. **Variance** — you can't pass `list[Dog]` where `list[Animal]` is expected
3. **Mutable default arguments** — the classic `def f(items=[])` foot-gun, but with a typing twist
4. **Missing return in some branches** — a function annotated `-> int` that only returns in some branches

Fix each. Some fixes will be "restructure the code", others "reach for `Sequence` instead of `list`", others "guard with `assert`". Try to pick the *narrowest* fix each time.

## What you'll practise

- Type narrowing with `isinstance`, `is not None`, `assert`
- The `Sequence[T]` / `Iterable[T]` covariant escape hatch
- When and where `# pyrefly: ignore[code]` is legitimate
- Reading `[error-code]` labels and using them to look up docs

## Rules

- No changing an annotation to a broader type just to hide an error. Fix the code, or use a more precise container (`Sequence`).
- You may use one `# pyrefly: ignore` — but only where the type system genuinely can't express the invariant. There is at most one such case in this file. If you find yourself reaching for it more than once, you're papering over a real bug.

Ask an instructor if you'd like to see a reference solution.
