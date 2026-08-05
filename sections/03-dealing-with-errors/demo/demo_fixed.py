"""End state of the Section 3 live demo — all type errors resolved."""


def total_price(items: list[dict[str, int]]) -> int | str:
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    if total == 0:
        return "sold out"
    return total


def first_name(full_name: str | None) -> str:
    if full_name is None:
        return ""
    return full_name.split(" ")[0]


class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


def contact_string(user: User) -> str:
    return f"{user.name} <{user.email}>"


def load_config(path: str) -> dict[str, str | int]:
    return {"port": 8080, "host": "localhost"}


if __name__ == "__main__":
    print(total_price([{"price": 3, "quantity": 2}]))
    print(first_name("Abby Mitchell"))
    print(contact_string(User("Abby", "abby@example.com")))
    print(load_config("app.toml"))
