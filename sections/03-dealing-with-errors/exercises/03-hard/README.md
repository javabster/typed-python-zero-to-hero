# Section 3 — Hard: Fix a small multi-file project

**Goal:** Practise diagnosing type errors that span *multiple* files, the way real-world debugging works. This is a small task-tracker CLI split across six files.

## Project structure

```
starter/
  __init__.py
  models.py        # Task, TaskStore, Priority
  storage.py       # save/load to a JSON file
  api.py           # thin functions used by the CLI
  filters.py       # filtering helpers (has some genuinely tricky variance issues)
  cli.py           # argparse-style entrypoint
  main.py          # runs a small scripted scenario
```

## What to do

1. Run pyrefly across the whole project:

   ```bash
   pyrefly check sections/03-dealing-with-errors/exercises/03-hard/starter/
   ```

2. You should see around 9 errors spread across the files. **Start at the file with the most-fundamental errors** — usually that's `models.py` (its errors cause secondary errors in files that import it).

3. Fix each error. Re-run pyrefly. Many errors will disappear as you fix upstream types.

4. Once pyrefly reports 0 errors, run `python -m starter.main` to confirm nothing broke at runtime.

## What you'll practise

- Reading errors across files
- Recognising when an error is a **symptom** of a bug in another file
- Deciding whether to fix the annotation, the code, or the caller
- Handling Optional/None propagation across module boundaries
- Using `TypedDict` and `Literal` types across files

## Rules

- No `# type: ignore` unless the type system genuinely cannot express the invariant. There is at most one such case in this project.
- The public-facing behaviour in `main.py` should stay the same. If it currently works, it should still work when you're done.

## Reference solution

A cleaned-up solution is available on request — ask an instructor. No peeking until you've tried!
