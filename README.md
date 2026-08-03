# Typed Python: from Zero to Hero

**PyCon AU 2026 Tutorial** — Abby Mitchell (with Conner?)

A hands-on tutorial for adopting type annotations in Python. We'll walk from the basics of annotating an untyped codebase all the way through advanced typing features, resolving type errors, and setting up a typechecker (using [Pyrefly](https://pyrefly.org)) in a dummy project. Feel free to work through these exercises at your own pace, ask questions and work with others if you wish. If you'd like help getting Pyrefly set up in your own project, just ask a member of the Pyrefly team to help you!

---

## Agenda (3 hours)

| Time        | Section                              | Focus                                                             |
|-------------|--------------------------------------|-------------------------------------------------------------------|
| 0:00–0:15   | Intro & Setup                        | Welcome, agenda, environment check                                |
| 0:15–1:00   | **Section 1**: Adding Annotations    | Basic types, functions, classes, simple containers                |
| 1:00–1:45   | **Section 2**: Advanced Typing       | Generics, unions, protocols, literals                             |
| 1:45–2:30   | **Section 3**: Dealing With Errors   | Running pyrefly, reading errors, refactoring to fix them          |
| 2:30–3:00   | **Section 4**: Setting Up Pyrefly    | Install, configure, run in CI                                     |

Each section is a ~15 min demo followed by ~30 min of hands-on exercises.

## "Choose Your Own Adventure"

Every exercise comes in three difficulty levels:

- **easy** — you've barely touched type annotations before
- **intermediate** — you're comfortable with the basics
- **hard** — you want to stretch into the advanced stuff

Pick whichever fits. If you finish early, try the next level up, or move to the next section. Pyrefly team members will be roaming — flag one down if you get stuck.

## Repo Layout

```
sections/
  01-adding-annotations/
    README.md          # section overview + demo notes
    demo/              # live-demo code
    exercises/
      easy/            # each level has starter.py and README.md
      intermediate/
      hard/
  02-advanced-typing/
  03-dealing-with-errors/
  04-setup-typechecker/
example-project/       # small untyped project used in Section 4
```

## Setup

**Do this before the workshop if you can** — see [SETUP.md](./SETUP.md) for the full guide.

Quick version:

```bash
git clone https://github.com/<TODO>/pyconau26-typing-workshop.git
cd pyconau26-typing-workshop
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
pyrefly check --version
```

## During the Workshop

1. Open the section folder you're working on
2. Read the section `README.md`
3. Pick a difficulty level — open `exercises/<level>/README.md`
4. Edit `starter.py`
5. Once you're happy — or stuck — flag down an instructor. Reference solutions are available on request.

## After the Workshop

The repo stays here as a reference. The [pyrefly docs](https://pyrefly.org) are the best next stop, and the [Python typing docs](https://docs.python.org/3/library/typing.html) cover every feature we touch and many we don't.
