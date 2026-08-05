"""EASY — annotate with unions and optionals."""


def find_user(users, target_id):
    """`users` is a list of dicts with 'id' and 'name' keys.
    `target_id` may be an int or a string of digits.
    Returns the matching dict, or None if not found."""
    tid = int(target_id) if isinstance(target_id, str) else target_id
    for user in users:
        if user["id"] == tid:
            return user
    return None


def first_matching(items, predicate):
    """Return the first item for which `predicate(item)` is truthy, or None."""
    for item in items:
        if predicate(item):
            return item
    return None


def parse_bool(value):
    """Accepts a bool, an int (0/1), or a str ('true'/'false', case-insensitive).
    Returns the corresponding bool, or None if the value can't be parsed."""
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value != 0
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered == "true":
            return True
        if lowered == "false":
            return False
    return None


def get_config(key):
    """Look up a config value by key. Returns:
    - "port" -> int
    - "host" -> str
    - "debug" -> bool
    - anything else -> None
    """
    if key == "port":
        return 8080
    if key == "host":
        return "localhost"
    if key == "debug":
        return False
    return None


if __name__ == "__main__":
    users = [{"id": 1, "name": "Abby"}, {"id": 2, "name": "Conner"}]
    print(find_user(users, "1"))
    print(first_matching([1, 2, 3, 4], lambda x: x > 2))
    print(parse_bool("TRUE"), parse_bool(0), parse_bool("nope"))
    print(get_config("port"), get_config("host"), get_config("missing"))
