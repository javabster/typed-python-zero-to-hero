"""Live-demo starting point for Section 3.

This module has several planted type errors. We'll run pyrefly on it live
and fix each one. See demo_fixed.py for the end state.
"""


def total_price(items: list[dict[str, int]]) -> int:
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    # Error 1: assigning a str to a variable pyrefly has inferred as int.
    total = "sold out" if total == 0 else total
    return total


def first_name(full_name: str | None) -> str:
    # Error 2: calling .split on a possibly-None value.
    return full_name.split(" ")[0]


class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


def contact_string(user: User) -> str:
    # Error 3: attribute typo.
    return f"{user.name} <{user.emial}>"


def notify(users: list[User], template: str) -> list[str]:
    # Error 4: passing an int where a str is expected.
    return [template.format(name=u.name, id=u) for u in users]


def load_config(path: str) -> dict[str, str]:
    # Error 5: return type says dict[str, str] but the values are mixed.
    return {"port": 8080, "host": "localhost"}


if __name__ == "__main__":
    print(total_price([{"price": 3, "quantity": 2}]))
    print(first_name("Abby Mitchell"))
    print(contact_string(User("Abby", "abby@example.com")))
    print(notify([User("Abby", "a@b.com")], "hello {name}"))
    print(load_config("app.toml"))
