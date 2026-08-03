# Setup Guide

Follow the steps below before attempting the exercises.

## Requirements

- Python **3.10 or newer** (3.12 recommended)
- `git`
- A code editor. VS Code with the Pyrefly extension is a great combination, but anything works.

Check your Python version:

```bash
python3 --version
```

## 1. Clone the repo

```bash
git clone https://github.com/<TODO>/pyconau26-typing-workshop.git
cd pyconau26-typing-workshop
```

## 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
# .venv\Scripts\activate        # Windows PowerShell
```

## 3. Install dependencies

```bash
pip install -e .
```

This installs:
- `pyrefly` — the typechecker we'll use throughout
- `numpy` — used in a few exercises
- `pytest` — for the small test files sprinkled through the exercises

## 4. Verify

```bash
pyrefly --version
pyrefly check sections/03-dealing-with-errors/demo/demo.py
```

You should see a version number, and then a handful of type errors from the demo file (that one has intentional bugs planted in it — 5 errors is the expected number). Seeing the errors means your install works.

> **Note:** running pyrefly on `sections/01-adding-annotations/demo/demo.py` will report **0 errors** — that's expected. That file is untyped but not *wrong*. Pyrefly (like most typecheckers) only flags actual type mismatches by default, not missing annotations.

## 5. (Optional but recommended) Editor integration

Pyrefly ships a language server. In VS Code, install the **Pyrefly** extension for inline error squiggles as you type. Other editors: see [pyrefly.org/docs/editor-setup](https://pyrefly.org/docs/editor-setup).

## Troubleshooting

- **`pyrefly: command not found`** — your venv isn't activated. Re-run the `source .venv/bin/activate` step.
- **`pip install` fails** — make sure you're on Python 3.10+. Older Pythons don't support some of the syntax we'll use.
- **Anything else** — grab a Pyrefly team member on the day.
