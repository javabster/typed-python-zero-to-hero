# Section 4 — Easy: Run pyrefly and read the errors

**Goal:** Run pyrefly on a real project, read its output, and fix at least one bug it finds. Every error you'll see corresponds to a **real runtime bug** — the annotations are honest; the code is what's broken.

## What to do

1. Change into the example project:

   ```bash
   cd example-project/
   ```

2. Verify pyrefly is installed (it should be from the workshop's top-level install):

   ```bash
   pyrefly --version
   ```

3. Look around before you run anything:

   ```bash
   ls
   cat pyproject.toml
   ```

   The project already has a minimal `[tool.pyrefly]` block in `pyproject.toml` — just `python-version = "3.12"`. Enough to enable checking, nothing custom yet.

4. Run pyrefly:

   ```bash
   pyrefly check
   ```

   You should see **8 errors**. Read them from top to bottom.

5. Pick any one error and **trace the runtime crash it prevents**. For example:

   - `server.py` line 34 — pyrefly says `'NoneType' has no 'visit'`. Look at the code: `link = _STORE.resolve(code); target = link.visit()`. What happens at runtime if `code` isn't in the store? (Answer: `resolve()` returns `None`, and `None.visit()` crashes with an `AttributeError`.)

   - `models.py` describe method — same category. `link.target` on a `None`. Would crash for any unknown code.

   - `tests/test_models.py` — a test is passing `12345` (an int) to a function that wants a `str`. Would crash with `TypeError`.

6. **Fix one bug.** For the None-check bugs, add `if link is None: ...`. For the wrong-type test, change `12345` to `"12345"`.

7. Re-run `pyrefly check`. Confirm the error count went down.

## What you'll practise

- Running pyrefly at the project level
- Reading its error messages and mapping each to a real runtime failure
- The core loop of typechecker-driven development: **fix, re-run, watch the count drop**

## Success criteria

- `pyrefly check` runs cleanly (no config errors)
- You can articulate what runtime crash each error prevents
- You've fixed at least one bug and confirmed the error count went down
