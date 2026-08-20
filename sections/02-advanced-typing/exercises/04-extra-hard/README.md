# Section 2 — Extra-Hard: Overloads and ParamSpec

**Goal:** Two independent tasks in one file. Part A tightens a function whose return type depends on its args using `@overload`. Part B rewrites a decorator factory using `ParamSpec` so the wrapped function keeps its real signature.


## What to do

Open [`starter.py`](./starter.py). Instructions live in the two comment banners at the top of each part.

Run:

```bash
pyrefly check sections/02-advanced-typing/exercises/04-extra-hard/starter.py
```

### Part A — `@overload`

`fetch(url, format)` returns a different type depending on the `format` string. Right now every caller gets `dict[str, Any] | str | bytes` back and has to isinstance-check. Add three `@overload` stubs on top of the implementation so pyrefly picks the exact return type from the `Literal` format.

### Part B — `ParamSpec`

`retry(times)` is a decorator factory. Its current annotations use `Any` everywhere, so pyrefly can't see the wrapped function's real signature. Use `ParamSpec` (and a `TypeVar` for the return type) to preserve the full signature — including catching wrong argument types at the call site.

Reference (Pyre docs, same feature works in pyrefly): https://pyre-check.org/docs/errors/#decorator-factories

## What you'll practise

**Part A:**
- `@overload` — writing typed stubs above a single implementation
- `Literal["json"] | Literal["text"]` for switching on a string arg
- Understanding that `@overload` is a **type-checker** construct, the stubs have no runtime effect

**Part B:**
- `ParamSpec` (`P`) — captures "all the parameters" of a callable
- Using `*args: P.args, **kwargs: P.kwargs`
- Composing `ParamSpec` with a `TypeVar` for the return type
- PEP 695 shorthand: `def retry[**P, R](times: int) -> ...`

## Hints

### Part A

- All three overload stubs use `...` as the body — they have no runtime effect.
- The order of overloads matters: pyrefly picks the first stub whose types match. Put the more specific ones first.
- Do **not** decorate the implementation itself with `@overload` — only the stubs.

### Part B

- The pre-3.12 form:
  ```python
  from collections.abc import Callable
  from typing import ParamSpec, TypeVar

  P = ParamSpec("P")
  R = TypeVar("R")

  def retry(times: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
      def decorator(fn: Callable[P, R]) -> Callable[P, R]:
          def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
              ...
          return wrapper
      return decorator
  ```
- The PEP 695 form (3.12+):
  ```python
    # work by defining the inside functions out for an easier time
    def retry(times: int): # returns a callable that takes in a callable and returns a callable
        def decorator(fn): # takes a callable and returns a callable
            def wrapper(*args, **kwargs): # we don't know what the types of the args and kwargs should be (check out ParamSpec!)
  ```
- `P.args` / `P.kwargs` are the only way to spread a `ParamSpec` — you can't use `P` on its own for `*args`.

## Bonus

- **Part A bonus:** what happens if you add a fourth call site with `format="xml"`? Which overload does pyrefly pick? What error do you get?
- **Part B bonus:** add a `Concatenate[LoggerAdapter, P]` to the decorator so the wrapper injects an extra first argument before the original `P` parameters.
