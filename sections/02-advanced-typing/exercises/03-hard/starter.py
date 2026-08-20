"""HARD — protocols + literals.

Introduce a Plugin protocol so that PluginRegistry.register only accepts
plugin-shaped objects. Then tighten the Job.state field to a Literal type
and make `transition` reject invalid state changes.
"""


class PluginRegistry:
    def __init__(self) -> None:
        # TODO: type this properly
        self._plugins: list = []

    def register(self, plugin) -> None:
        """Add a plugin. Should ONLY accept objects satisfying the Plugin protocol."""
        self._plugins.append(plugin)

    def run_all(self, payload: bytes) -> list[bytes]:
        return [p.run(payload) for p in self._plugins]

    def names(self) -> list[str]:
        return [p.name for p in self._plugins]


class Job:
    def __init__(self, name: str) -> None:
        self.name = name
        # TODO: state should be one of "pending", "running", "done", "failed"
        self.state: str = "pending"


def transition(job: Job, new_state: str) -> None:
    """Move `job` to `new_state`. Only these transitions are valid:
        pending -> running
        running -> done
        running -> failed
    Any other transition should raise.

    TODO: change `new_state` from `str` to the `State` literal you defined for
    `Job.state`. Once you do, a call like `transition(job, "on-fire")` should
    be rejected by pyrefly at the call site, not just at runtime.
    """
    valid = {
        ("pending", "running"),
        ("running", "done"),
        ("running", "failed"),
    }
    if (job.state, new_state) not in valid:
        raise ValueError(f"Illegal transition {job.state} -> {new_state}")
    job.state = new_state


def describe(state: str) -> str:
    """Human-readable description of a state.

    TODO: rewrite this using `match state:` and `assert_never` in the default
    branch. Once `state` is typed as `State`, pyrefly will use the match to
    check that every literal is covered — if you later add a new state (say
    "cancelled") to `State`, the missing `case` becomes a type error.
    """
    if state == "pending":
        return "waiting to start"
    if state == "running":
        return "in progress"
    if state == "done":
        return "completed successfully"
    if state == "failed":
        return "encountered an error"
    raise ValueError(f"unknown state: {state}")


# --- concrete plugin implementations (do NOT modify) ---


class UppercasePlugin:
    """Plugin that converts payload to upper-case."""
    name = "uppercase"

    def setup(self, config: dict[str, str]) -> None:
        self.encoding = config.get("encoding", "utf-8")

    def run(self, payload: bytes) -> bytes:
        return payload.decode(self.encoding).upper().encode(self.encoding)


class ReversePlugin:
    """Plugin that reverses payload bytes."""
    name = "reverse"

    def setup(self, config: dict[str, str]) -> None:
        pass

    def run(self, payload: bytes) -> bytes:
        return payload[::-1]


if __name__ == "__main__":
    uppercase = UppercasePlugin()
    uppercase.setup({"encoding": "utf-8"})
    reverse = ReversePlugin()
    reverse.setup({})

    registry = PluginRegistry()
    registry.register(uppercase)
    registry.register(reverse)
    print(registry.names())
    print(registry.run_all(b"hello"))

    job = Job("nightly-etl")
    transition(job, "running")
    print(describe(job.state))
    transition(job, "done")
    print(describe(job.state))
