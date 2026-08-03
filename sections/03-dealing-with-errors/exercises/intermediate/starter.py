"""INTERMEDIATE — subtler type errors."""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."


class Dog(Animal):
    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow"


# BUG A: mutable default argument — and its type is inferred loosely.
def collect(item, seen=[]):
    seen.append(item)
    return seen


# BUG B: variance. `feed_all` mutates its list; callers that pass a
# `list[Dog]` will be surprised when the function tries to append a Cat.
# Rework the signature so the incorrect call site is caught by pyrefly.
def feed_all(animals: list[Animal]) -> None:
    for a in animals:
        print(f"feeding {a.name}")
    # Notice this line — appending is what makes list-variance a real problem.
    animals.append(Cat("whiskers"))


# BUG C: narrowing failure.
def loud_name(animal: Animal | None) -> str:
    # pyrefly can't tell that a helper `is_present` narrows `animal` to Animal.
    # Restructure this so it can.
    if is_present(animal):
        return animal.name.upper()
    return ""


def is_present(x: object | None) -> bool:
    return x is not None


# BUG D: missing return.
def clamp(n: int, lo: int, hi: int) -> int:
    if n < lo:
        return lo
    if n > hi:
        return hi
    # forgot to return the passed-through case


if __name__ == "__main__":
    a = collect("first")
    b = collect("second")   # b is not a fresh list! silent bug.
    print("collect leaks:", a, b)

    dogs: list[Dog] = [Dog("Rex"), Dog("Buddy")]
    feed_all(dogs)
    for d in dogs:
        print(d.speak())

    print(loud_name(Dog("Rex")))
    print(clamp(5, 0, 10))
