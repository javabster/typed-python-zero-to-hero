"""Generate short codes for URLs. Fully typed."""

import hashlib

ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"


def short_code(url: str, length: int = 6) -> str:
    digest = hashlib.sha256(url.encode()).digest()
    n = int.from_bytes(digest[:8], "big")
    out: list[str] = []
    base = len(ALPHABET)
    while len(out) < length:
        out.append(ALPHABET[n % base])
        n //= base
    return "".join(out)
