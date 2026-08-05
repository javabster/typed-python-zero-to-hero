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
        # TODO: state should be Literal["pending", "running", "done", "failed"]
        self.state: str = "pending"


def transition(job: Job, new_state: str) -> None:
    """Move `job` to `new_state`. Only these transitions are valid:
        pending -> running
        running -> done
        running -> failed
    Any other transition should raise.
    Once the state field is a Literal, pyrefly should catch bad literal values
    passed here as `new_state`.
    """
    valid = {
        ("pending", "running"),
        ("running", "done"),
        ("running", "failed"),
    }
    if (job.state, new_state) not in valid:
        raise ValueError(f"Illegal transition {job.state} -> {new_state}")
    job.state = new_state


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
    registry = PluginRegistry()
    registry.register(UppercasePlugin())
    registry.register(ReversePlugin())
    print(registry.names())
    print(registry.run_all(b"hello"))

    job = Job("nightly-etl")
    transition(job, "running")
    transition(job, "done")
    print(job.state)
