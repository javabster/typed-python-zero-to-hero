# Section 4 — Easy: Get pyrefly running on the example project

**Goal:** Install pyrefly on a fresh, untyped project and run your first check.

## What to do

1. Change into the example project:

   ```bash
   cd example-project/
   ```

2. Verify pyrefly is installed (it should be from the workshop's top-level install):

   ```bash
   pyrefly --version
   ```

   If not, `pip install pyrefly` inside your workshop venv.

3. Run pyrefly with no config:

   ```bash
   pyrefly check
   ```

   You should see a bunch of errors and warnings — that's expected. This project is intentionally untyped.

4. Count the errors. Pick any *one* file (start with `example_project/models.py`) and add just enough type annotations that pyrefly is happy about that file.

5. Re-run `pyrefly check`. How many errors are left?

## What you'll practise

- Running pyrefly at the project level (not just on a single file)
- Reading total error counts and finding "quick wins"
- Prioritising which module to type first (usually the leaf modules with no imports)

## Success criteria

- `pyrefly check` runs without crashing
- You've reduced the total error count by at least one file's worth
- You know how to interpret the summary line pyrefly prints at the end
