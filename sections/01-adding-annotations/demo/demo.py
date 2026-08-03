"""Live-demo starting point: an untyped mini script we'll annotate together."""


def greet(name):
    return f"Hello, {name}!"


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def word_counts(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


class Cart:
    def __init__(self):
        self.items = []
        self.discount = None

    def add(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def subtotal(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def total(self):
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
