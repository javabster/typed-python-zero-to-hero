# example-project

A small, mostly-typed Python project used in the **Section 4** exercises. It's a toy URL shortener with a handful of real latent bugs planted for you to find with Pyrefly.

Layout:

- `src/example_project/models.py` — the `ShortLink` domain object and `LinkStore` (1 real bug: missing None check in `describe`)
- `src/example_project/hashing.py` — a short-code generator (clean, no bugs)
- `src/example_project/server.py` — a `wsgiref`-based HTTP wrapper (1 real bug: missing None check before `link.visit()`)
- `src/example_project/legacy.py` — a deliberately messy older module with 4 real runtime bugs. Section 4 shows how to *downgrade* these to warnings without blocking CI.
- `tests/test_models.py` — a couple of sanity tests, plus one test with a real type mistake
- `pyproject.toml` — normal project metadata plus a bare-bones `[tool.pyrefly]` block (just `python-version`); Section 4 exercises grow it into something real

Every "bug" here is a genuine mistake that would crash at runtime — pyrefly reads the correct annotations and finds them.

## Run it

```bash
cd example-project/
pip install -e .
python -m example_project.server
# then in another terminal:
curl -X POST http://localhost:8000/ -d 'https://pycon.org.au'
curl http://localhost:8000/<code_returned_above>
```

(Warning: some of the planted bugs will crash the server on unexpected inputs — that's the point.)

## Test it

```bash
pytest
```

## Type-check it

```bash
pyrefly check
# should report 8 errors on first run
```
