# Section 2 — Hard: Protocols and Literals

**Goal:** Design a plugin registry that accepts any object satisfying a `Protocol`, and use `Literal` types to model a state machine.

## What to do

Open [`starter.py`](./starter.py). It contains a `PluginRegistry` that currently accepts anything and a `Job` class with a stringly-typed `state` field. Your job:

1. **Define a `Plugin` `Protocol`** with the methods a plugin must expose (`name` property, `setup(config: dict[str, str]) -> None`, `run(payload: bytes) -> bytes`). Update `PluginRegistry.register` to accept only `Plugin`.
2. **Convert `state`** from `str` to a `Literal[...]` covering only the valid states.
3. **Change `transition`'s `new_state` parameter** from `str` to your `State` literal. This is what makes a call like `transition(job, "on-fire")` a type error at the call site rather than a runtime `ValueError`.
4. **Rewrite `describe`** to use a `match` statement on `state` with an `assert_never(state)` in the default branch. Once `state` is a `Literal`, pyrefly will treat `assert_never` as an exhaustiveness check and if you later add a new state to `State` and forget to add a `case`, pyrefly rejects it.

Do **not** modify the concrete plugin classes at the bottom of the file — they should already satisfy the `Protocol` structurally. That's the whole point.

Run:

```bash
pyrefly check sections/02-advanced-typing/exercises/03-hard/starter.py
```

## What you'll practise

- Structural typing with `Protocol` (no inheritance required)
- `Literal` for enum-like string values
- `assert_never` for exhaustiveness checks on `Literal`/`match`
- Narrowing `Literal` types across a `match` statement

## Hints

- `Protocol` classes go in `typing`. Methods in the protocol body use `...` as the body — they're purely structural.
- If you want the protocol to be usable with `isinstance()`, decorate it with `@runtime_checkable`. Not required for pyrefly.
- For state, a `type State = Literal["pending", "running", "done", "failed"]` alias reads best.
- To get exhaustiveness in a `match`, add a `case _: assert_never(state)` at the end.

## Bonus

Add a `Plugin` that intentionally violates the protocol (missing a method, wrong type). Confirm pyrefly rejects it when passed to `register`.
