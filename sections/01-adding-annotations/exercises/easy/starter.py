"""EASY — annotate these functions.

Add type annotations to every parameter and return value below.
Run `pyrefly check` on this file when you're done.
"""


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def shout(message):
    return message.upper() + "!"


def print_banner(text, char="="):
    line = char * len(text)
    print(line)
    print(text)
    print(line)


def divide(numerator, denominator):
    if denominator == 0:
        return None
    return numerator / denominator


def first_and_last(items):
    return items[0], items[-1]


def counts_by_letter(word):
    result = {}
    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    return result


def clamp(value, low=0, high=100):
    if value < low:
        return low
    if value > high:
        return high
    return value
