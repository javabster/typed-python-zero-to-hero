"""Generate short codes for URLs. Intentionally not annotated."""

import hashlib

ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"


def short_code(url, length=6):
    digest = hashlib.sha256(url.encode()).digest()
    n = int.from_bytes(digest[:8], "big")
    out = []
    base = len(ALPHABET)
    while len(out) < length:
        out.append(ALPHABET[n % base])
        n //= base
    return "".join(out)
