# Section 4 — Hard: Set up pyrefly in CI (or on your own project)

**Goal:** Wire pyrefly into a CI pipeline so it runs on every push and pull request. Two paths — pick one:

## Path A — Use the example project

1. Copy [`../../demo/github-workflow.yml`](../../demo/github-workflow.yml) into `example-project/.github/workflows/pyrefly.yml`.
2. Adjust the `install` step to reference the example project's dependencies.
3. Adjust the `run` step to `pyrefly check` from the correct directory.
4. (Optional) Push the project up to a personal GitHub repo and confirm the workflow runs.
5. **Bonus:** add a matrix so pyrefly runs on Python 3.10, 3.11, and 3.12.
6. **Bonus:** make the CI job fail if error count *increases* from `main`, using pyrefly's baseline / diff-check features.

## Path B — Bring your own project

Grab a Pyrefly team member — we'll help you:

1. Install pyrefly in your project (`pip install pyrefly` or the equivalent in your package manager)
2. Run `pyrefly init` to generate a baseline config
3. Triage the first wave of errors — decide what to fix now vs. exclude vs. downgrade
4. Wire it into your CI of choice (GitHub Actions, GitLab CI, CircleCI, Buildkite — all fine)
5. Talk through a rollout plan for your team

## What you'll practise

- Real project onboarding — this is the highest-value skill from the workshop
- Balancing "correct" with "shippable" (excludes, warn-vs-error severity, per-module overrides)
- Writing a lightweight CI job

## Success criteria

- Path A: A committed `.github/workflows/pyrefly.yml` that would successfully run pyrefly on PR.
- Path B: A clean `pyrefly check` on some meaningful subset of your project, with a plan for the rest.
