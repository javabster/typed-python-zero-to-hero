# Section 4: Setting Up Pyrefly

**Time:** 30 min (10 min demo + 20 min exercises)

## What you'll learn

- How to install and initialise Pyrefly on any Python project
- Configuring Pyrefly with `pyrefly.toml` or a `[tool.pyrefly]` block in `pyproject.toml`
- Common configuration knobs: includes/excludes, per-module overrides, strictness
- Editor setup (LSP)
- Running Pyrefly in CI with GitHub Actions

## Demo

We'll take the [`example-project/`](../../example-project/) — a small, mostly-typed URL shortener with a handful of real latent bugs — and grow its Pyrefly setup live:

1. `pyrefly check` — see what its bare-bones starter config catches (8 errors)
2. Add `project-includes`/`project-excludes` to scope what gets checked
3. Add a `[[sub-config]]` block that downgrades the legacy module's errors to warnings
4. Add a GitHub Actions workflow so pyrefly runs on every PR

Every error you see is a **real runtime bug** — `AttributeError`, `TypeError`, and friends. The annotations are honest; Pyrefly reads them and finds the crashes waiting to happen.

See [`demo/pyproject.toml`](./demo/pyproject.toml) and [`demo/github-workflow.yml`](./demo/github-workflow.yml) for the reference config files.

## Exercises

| Level          | What to do                                                    |
|----------------|---------------------------------------------------------------|
| [easy](./exercises/01-easy/)                 | Run pyrefly on `example-project/`, read the 8 errors, fix at least one   |
| [intermediate](./exercises/02-intermediate/) | Extend the `[tool.pyrefly]` block with includes/excludes and a per-module override |
| [hard](./exercises/03-hard/)                 | Set up pyrefly in CI (or on your own project — help from the team!)      |

## Common config knobs

```toml
# In pyproject.toml
[tool.pyrefly]
# Which files to include (default is smart, but you can override)
project-includes = ["src/**/*.py"]
project-excludes = ["**/tests/**", "**/vendor/**"]

# Python version to target
python-version = "3.12"

# Per-module overrides — glob paths, valid error-kind names
[[tool.pyrefly.sub-config]]
matches = "**/legacy.py"
[tool.pyrefly.sub-config.errors]
missing-attribute = "warn"   # downgrade a whole category for this module
bad-return = "warn"
```

## Suggested rollout path for real projects

1. Install pyrefly and add a minimal config (`pyrefly.toml` or `[tool.pyrefly]`)
2. Run `pyrefly check` — look at the numbers, not each error
3. Add excludes for legacy modules or test-only code you don't want to fix yet, or downgrade them to `warn`
4. Fix the errors in your "core" modules first
5. Turn on CI once the check is green
6. Gradually remove excludes / warn-downgrades as you fix each subsystem
