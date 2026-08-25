"""Live-demo starting point for Section 3.

This module has 5 planted type errors. We'll run pyrefly on it live
and fix each one. See demo_fixed.py for the end state.
"""


def total_price(items: list[dict[str, int]]) -> int:
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    # Error 1: `total` starts out an int, then gets a str stuffed into it.
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


def load_config(path: str) -> dict[str, str]:
    # Error 4: return type says dict[str, str] but the values are mixed.
    return {"port": 8080, "host": "localhost"}


class Admin(User):
    pass


# Error 5: variance. `print_all` only reads from `users`, so a `list[Admin]`
# *ought* to be assignable to a `list[User]` — but `list[T]` is invariant.
# The fix is to accept a covariant read-only container.
def print_all(users: list[User]) -> None:
    for u in users:
        print(u.name)


if __name__ == "__main__":
    print(total_price([{"price": 3, "quantity": 2}]))
    print(first_name("Abby Mitchell"))
    print(contact_string(User("Abby", "abby@example.com")))
    print(load_config("app.toml"))

    admins: list[Admin] = [Admin("Abby", "abby@example.com")]
    print_all(admins)   # pyrefly rejects this — see Error 5.
