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


# BUG A: mutable default argument. The `[]` is built ONCE, when Python
# executes the `def`, and every call that omits `seen` shares that same list.
#
# Heads up: pyrefly reports NOTHING here, even though the annotations are
# complete and correct. A typechecker catches type mismatches, not every
# logic bug — this one is a job for a linter (ruff's B006) or your own eyes.
# Fix it anyway; the `if __name__` block below shows the damage.
def collect(item: str, seen: list[str] = []) -> list[str]:
    seen.append(item)
    return seen


# BUG B: variance. This function MUTATES the list it's handed — it appends a
# Cat. That's exactly why `list[T]` is invariant: pyrefly rejects the call
# site below that passes a `list[Dog]`, because letting it through would
# smuggle a Cat into a list its owner believes holds only Dogs.
#
# The signature here is already right. Fix the CALLER.
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
    feed_all(dogs)   # pyrefly rejects this — see BUG B.
    for d in dogs:
        print(d.speak())

    print(loud_name(Dog("Rex")))
    print(clamp(5, 0, 10))
