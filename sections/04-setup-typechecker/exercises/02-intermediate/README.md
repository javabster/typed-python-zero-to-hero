# Section 4 — Intermediate: Extend the pyrefly config

**Goal:** Take the bare-bones `[tool.pyrefly]` block in `example-project/pyproject.toml` and grow it into something that reflects a real project's needs — scoped includes, targeted excludes, and per-module severity overrides.

## Starting point

```bash
cd example-project/
pyrefly check
```

You should see **8 errors** (with the minimal starter config). Your job: get to **3 errors + 4 hidden warnings** by improving the config, without changing any source code.

## What to do

Open `example-project/pyproject.toml`. Extend the `[tool.pyrefly]` block to:

1. **Restrict includes to `src/`.** Tests shouldn't be typechecked at this level yet — they often have their own patterns. (This should drop the count from 8 → 7.)
2. **Exclude `**/tests/**` and `**/build/**`.**
3. **Downgrade legacy errors to warnings.** Add a `[[tool.pyrefly.sub-config]]` block matching `**/legacy.py` that turns `missing-attribute`, `unsupported-operation`, and `bad-return` into `warn`. (This should drop visible errors from 7 → 3, and make `pyrefly check` exit 0.)

Then verify:

```bash
pyrefly check
# should show: INFO 3 errors (4 warnings not shown)
echo $?
# should show: 0

pyrefly check --min-severity warn
# should show: INFO 7 diagnostics — the 4 legacy ones tagged WARN, the other 3 as ERROR
```

## What you'll practise

- Configuring pyrefly via a `[tool.pyrefly]` block in `pyproject.toml`
- Glob patterns for `project-includes` / `project-excludes`
- Per-module overrides with `[[tool.pyrefly.sub-config]]` — the primary tool for rolling out typing to legacy code
- The distinction between exit-code failures and informational warnings

## Hints

- `[[tool.pyrefly.sub-config]]` uses double square brackets — that's TOML syntax for "an object in an array". You can have multiple such blocks for multiple modules.
- The `matches` field takes a glob path (not a Python module name). `**/legacy.py` works.
- Setting an error kind to `"warn"` is one option; other valid severities are `"error"`, `"info"`, `"ignore"`.
- If you split the config into its own file (`pyrefly.toml` at the project root, no `tool.pyrefly.` prefix on any key), pyrefly picks it up too. `pyrefly.toml` wins over `pyproject.toml` if both exist.

## Bonus

- Add a second `[[tool.pyrefly.sub-config]]` block matching `**/server.py` that downgrades JUST `missing-attribute` to `warn`. Verify only the server.py error is affected.

## Reference

See [`../../demo/pyproject.toml`](../../demo/pyproject.toml) for a full example config.
