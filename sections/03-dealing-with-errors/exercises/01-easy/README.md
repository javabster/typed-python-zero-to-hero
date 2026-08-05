# Section 3 — Easy: Find and fix the errors

**Goal:** Get comfortable running pyrefly, reading its output, and applying the obvious fix.

## What to do

1. Run pyrefly on the starter file:

   ```bash
   pyrefly check sections/03-dealing-with-errors/exercises/01-easy/starter.py
   ```

2. Read the errors from top to bottom. There are **5 planted errors**.
3. Fix each one. The types are annotated correctly — the *code* is what's wrong.
4. Re-run pyrefly until it reports 0 errors.

## What you'll practise

- Reading a pyrefly error message
- Distinguishing "the code is wrong" from "the annotation is wrong"
- Basic fixes: typo, wrong literal type, missing conversion, missing `None` check, wrong attribute name

## Rules

- **Don't** change the type annotations to hide errors. Fix the underlying code.
- **Don't** use `# type: ignore`. It's a real tool but not the right one for these errors.
- **Do** re-run pyrefly frequently to see your progress.

Ask an instructor if you'd like to see a reference solution — but only after you've had a real go yourself.
