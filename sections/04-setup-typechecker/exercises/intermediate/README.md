# Section 4 — Intermediate: Configure pyrefly

**Goal:** Add a `[tool.pyrefly]` section to `example-project/pyproject.toml` that reflects the shape of a real-world project (source layout, excluded paths, targeted python version, per-module overrides).

## What to do

Open `example-project/pyproject.toml`. Add a `[tool.pyrefly]` block that:

1. **Includes only** the `src/` tree (currently the whole project gets checked, including tests and any scratch scripts).
2. **Excludes** `**/tests/**` and any `**/build/**` directories.
3. **Targets Python 3.12** explicitly.
4. **Adds a per-module override** downgrading errors in `example_project.legacy` from errors to warnings (that module represents older code we're still cleaning up).

Then re-run:

```bash
cd example-project/
pyrefly check
```

You should see:
- fewer files scanned (tests no longer included)
- errors in the `legacy` submodule appear as warnings instead of errors
- the exit code is 0 if only warnings remain

## What you'll practise

- Configuring pyrefly via `pyproject.toml`
- Understanding the difference between `project-includes`, `project-excludes`, and per-file `search-path`
- Setting per-module severity overrides — the primary tool for rolling out typing to legacy code

## Reference config

See [`../../demo/pyproject.toml`](../../demo/pyproject.toml) if you need a starting template.
