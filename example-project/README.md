# example-project

A small, intentionally-untyped Python project used in **Section 4** exercises. It's a toy URL shortener:

- `example_project/models.py` — the `ShortLink` domain object and an in-memory store
- `example_project/hashing.py` — a tiny "short code" generator
- `example_project/server.py` — a `wsgiref`-based HTTP wrapper (no third-party deps)
- `example_project/legacy.py` — an older, weirder implementation left in for the "per-module overrides" exercise
- `tests/test_models.py` — a couple of sanity tests
- `pyproject.toml` — currently *has no* `[tool.pyrefly]` section — that's yours to add.

## Run it

```bash
cd example-project/
pip install -e .
python -m example_project.server
# then in another terminal:
curl -X POST http://localhost:8000/ -d 'https://pycon.org.au'
curl http://localhost:8000/<code_returned_above>
```

## Test it

```bash
pytest
```

## Type-check it (once you've set up pyrefly)

```bash
pyrefly check
```
