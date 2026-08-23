# Typed Python: from Zero to Hero

**PyCon AU 2026 Workshop**

A hands-on tutorial for adopting type annotations in Python. We'll walk from the basics of annotating an untyped codebase all the way through advanced typing features, resolving type errors, and setting up a typechecker (using [Pyrefly](https://pyrefly.org)) in a dummy project. Feel free to work through these exercises at your own pace, ask questions and work with others if you wish. If you'd like help getting Pyrefly set up in your own project, just ask a member of the Pyrefly team to help you!

---

## Agenda (2 hours)

| Time (rough plan)       | Section                              | Focus                                                             |
|-------------|--------------------------------------|-------------------------------------------------------------------|
| 12:00–12:05   | Intro & Setup                        | Welcome, agenda, typing background
| 12:05–12:15   | **Section 1**: Adding Annotations    | Basic types, functions, classes, containers, callables            |
| 12:30–12:40   | **Section 2**: Advanced Typing       | Generics, unions, protocols, literals, overloads, ParamSpec       |
| 13:00–13:10   | **Section 3**: Dealing With Errors   | Running pyrefly, reading errors, variance, refactoring to fix them |
| 13:30–13:40   | **Section 4**: Setting Up Pyrefly    | Install, configure, run in CI                                     |

Each section includes a ~10 min demo followed by ~20 min of hands-on exercises. You're free to work at your own pace or tackle the exercises in any order you prefer

## "Choose Your Own Adventure"

Every exercise comes in three difficulty levels (Section 2 also has an *extra-hard*):

- **easy** — you've barely touched type annotations before
- **intermediate** — you're comfortable with the basics
- **hard** — you want to stretch into the advanced stuff

Pick whichever fits. If you finish early, try the next level up, or move to the next section. Flag down a facilitator if you get stuck

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
git clone https://github.com/javabster/typed-python-zero-to-hero.git
cd pyconau26-typing-workshop
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
pyrefly check --version
```

## During the Workshop

1. Open the section folder you're working on
2. Read the section `README.md`
3. Watch the live demo (run by workshop host) or read through it yourself
4. Pick a difficulty level — open `exercises/<level>/README.md`
5. Edit `starter.py`, use `pyrefly check <file-name>` to check there are no type errors
6. Once you're done move on to the next task, or flag down a workshop facilitator if you're stuck


## Resources

* [Official Python typing docs](https://docs.python.org/3/library/typing.html)
* [Python Typing 101](https://pyrefly.org/en/docs/python-typing-for-beginners/)
* [Pyrefly docs & sandbox](https://pyrefly.org)
