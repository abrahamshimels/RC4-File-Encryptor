#!/usr/bin/env python3
"""Encrypt a file in place with the RC4 stream cipher."""

from __future__ import annotations

import argparse
from pathlib import Path


def rc4_keystream(key: bytes) -> list[int]:
    """Generate the RC4 key schedule state."""
    s = list(range(256))
    j = 0
    key = list(key)

    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]

    return s


def rc4_crypt(data: bytes, key: bytes) -> bytes:
    """Encrypt or decrypt arbitrary bytes using the RC4 cipher."""
    s = rc4_keystream(key)
    i = 0
    j = 0
    output = bytearray()

    for byte in data:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        output.append(byte ^ s[(s[i] + s[j]) % 256])

    return bytes(output)


def encrypt_file(file_path: str | Path, key: str | bytes) -> None:
    """Read a file, encrypt it with RC4, and write it back in place."""
    target = Path(file_path)
    key_bytes = key.encode("utf-8") if isinstance(key, str) else key

    with target.open("rb") as file_handler:
        original = file_handler.read()

    encrypted = rc4_crypt(original, key_bytes)

    with target.open("wb") as file_handler:
        file_handler.write(encrypted)


def main() -> None:
    parser = argparse.ArgumentParser(description="Encrypt a file in place using RC4.")
    parser.add_argument("file", nargs="?", default="file.txt", help="File to encrypt.")
    parser.add_argument("--key", default="rc4-secret-key", help="RC4 encryption key.")
    args = parser.parse_args()

    try:
        encrypt_file(args.file, args.key)
    except FileNotFoundError:
        raise SystemExit(f"Error: file not found: {args.file}")

    print(f"Encrypted {args.file} using key: {args.key}")


if __name__ == "__main__":
    main()
