"""INTERMEDIATE — replace these two duplicate classes with a single generic Cache[T]."""


class IntCache:
    def __init__(self, capacity: int = 128) -> None:
        self.capacity = capacity
        self._store: dict[str, int] = {}
        self._order: list[str] = []

    def get(self, key: str) -> int | None:
        if key not in self._store:
            return None
        self._order.remove(key)
        self._order.append(key)
        return self._store[key]

    def set(self, key: str, value: int) -> None:
        if key in self._store:
            self._order.remove(key)
        elif len(self._store) >= self.capacity:
            oldest = self._order.pop(0)
            del self._store[oldest]
        self._store[key] = value
        self._order.append(key)

    def keys(self) -> list[str]:
        return list(self._order)


class StrCache:
    def __init__(self, capacity: int = 128) -> None:
        self.capacity = capacity
        self._store: dict[str, str] = {}
        self._order: list[str] = []

    def get(self, key: str) -> str | None:
        if key not in self._store:
            return None
        self._order.remove(key)
        self._order.append(key)
        return self._store[key]

    def set(self, key: str, value: str) -> None:
        if key in self._store:
            self._order.remove(key)
        elif len(self._store) >= self.capacity:
            oldest = self._order.pop(0)
            del self._store[oldest]
        self._store[key] = value
        self._order.append(key)

    def keys(self) -> list[str]:
        return list(self._order)


if __name__ == "__main__":
    ints = IntCache(capacity=3)
    ints.set("a", 1)
    ints.set("b", 2)
    print(ints.get("a"))

    strs = StrCache(capacity=3)
    strs.set("greeting", "hello")
    print(strs.get("greeting"))
