"""EASY — 5 planted type errors. Fix the code, not the annotations."""


def word_count(sentence: str) -> int:
    # BUG: returns a list, not an int.
    return sentence.split()


def average(numbers: list[float]) -> float:
    # BUG: dividing a list by an int.
    return numbers / len(numbers)


def greet(user: dict[str, str]) -> str:
    # BUG: attribute-style access on a dict.
    return f"Hello, {user.name}"


def double_all(items: list[int]) -> list[int]:
    # BUG: appending a str to a list[int].
    doubled: list[int] = []
    for item in items:
        doubled.append(str(item * 2))
    return doubled


def read_age(raw: str | None) -> int:
    # BUG: calling int() on possibly-None.
    return int(raw)


if __name__ == "__main__":
    print(word_count("hello world"))
    print(average([1.0, 2.0, 3.0]))
    print(greet({"name": "Abby"}))
    print(double_all([1, 2, 3]))
    print(read_age("42"))
