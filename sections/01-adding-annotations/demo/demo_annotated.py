"""Live-demo end state — the same script with type annotations added."""

from dataclasses import dataclass


def greet(name: str) -> str:
    return f"Hello, {name}!"


def average(numbers: list[float | int]) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def word_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


@dataclass
class CartItem:
    name: str
    price: float
    quantity: int


class Cart:
    items: list[CartItem]
    discount: float | None

    def __init__(self) -> None:
        self.items = []
        self.discount = None

    def add(self, name: str, price: float, quantity: int = 1) -> None:
        self.items.append(CartItem(name, price, quantity))

    def subtotal(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

    def total(self) -> float:
        st = self.subtotal()
        if self.discount is not None:
            st = st * (1 - self.discount)
        return st


if __name__ == "__main__":
    print(greet("PyCon AU"))
    print(average([1, 2, 3, 4, 5]))
    print(word_counts("hello world hello"))

    cart = Cart()
    cart.add("apple", 1.50, 3)
    cart.add("bread", 4.00)
    cart.discount = 0.10
    print(f"Total: ${cart.total():.2f}")
