# Section 4: Setting Up Pyrefly

**Time:** 30 min (10 min demo + 20 min exercises)

## What you'll learn

- How to install and initialise Pyrefly on any Python project
- Configuring Pyrefly with `pyrefly.toml` or a `[tool.pyrefly]` block in `pyproject.toml`
- Common configuration knobs: includes/excludes, per-module overrides, strictness
- Editor setup (LSP)
- Running Pyrefly in CI with GitHub Actions

## Demo

We'll take the [`example-project/`](../../example-project/) — an intentionally-untyped small Flask-style app — and add Pyrefly to it live:

1. `pip install pyrefly`
2. `pyrefly init` — auto-generate a starter config
3. Run `pyrefly check` and triage the first wave of errors
4. Configure `[tool.pyrefly]` to exclude tests, vendored code, etc.
5. Add a GitHub Actions workflow so pyrefly runs on every PR

See [`demo/pyproject.toml`](./demo/pyproject.toml) and [`demo/github-workflow.yml`](./demo/github-workflow.yml) for the reference config files.

## Exercises

| Level          | What to do                                                    |
|----------------|---------------------------------------------------------------|
| [easy](./exercises/easy/)                 | Install pyrefly in `example-project/` and run your first check          |
| [intermediate](./exercises/intermediate/) | Add a `pyproject.toml` config with excludes and strict overrides         |
| [hard](./exercises/hard/)                 | Set up pyrefly in CI (or on your own project — help from the team!)      |

## Common config knobs

```toml
# In pyproject.toml
[tool.pyrefly]
# Which files to include (default is smart, but you can override)
project-includes = ["src/**/*.py"]
project-excludes = ["**/tests/**", "**/vendor/**"]

# Python version to target
python-version = "3.12"

# Per-module overrides
[[tool.pyrefly.sub-config]]
matches = "src.legacy.*"
errors = { not-assignable = "warn" }   # downgrade a whole category
```

## Suggested rollout path for real projects

1. Install and run `pyrefly init` to get a baseline config
2. Run `pyrefly check` — look at the numbers, not each error
3. Add excludes for legacy modules or test-only code you don't want to fix yet
4. Fix the errors in your "core" modules first
5. Turn on CI once the check is green
6. Gradually remove excludes as you fix each subsystem
