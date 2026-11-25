#!/usr/bin/env python3
"""Entry for u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.

Writes one funny, true one-line review of the most boring everyday object
(the shower curtain) to /output/entry.txt. Deterministic: the same bytes on
every run, no network, no randomness, no clock.
"""
import hashlib
import os
import sys

REVIEW = "The shower curtain clings to my leg every morning like it is afraid of being alone in there. It is. That is the whole job."
EXPECTED_SHA256 = "0634a42d23dc732a431217898dd8229b608021ae60c0c3f07f9ed3262e14463c"
EXPECTED_BYTES = 122


def verify(path: str, data: bytes) -> bool:
    """Read back the written file and confirm it is byte-for-byte identical."""
    with open(path, "rb") as fh:
        written = fh.read()
    if len(written) != EXPECTED_BYTES:
        print(f"verify fail: file is {len(written)} bytes, expected {EXPECTED_BYTES}", file=sys.stderr)
        return False
    if written != data:
        print("verify fail: file bytes differ from entry", file=sys.stderr)
        return False
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"verify fail: file sha256 {digest}", file=sys.stderr)
        return False
    return True


def main() -> int:
    data = REVIEW.encode("utf-8")
    if not 1 <= len(data) <= 200:
        print(f"gate fail: {len(data)} bytes, need 1-200", file=sys.stderr)
        return 1
    if b"\n" in data:
        print("gate fail: review must stay on one line", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256 or len(data) != EXPECTED_BYTES:
        print(f"self-check fail: got {len(data)} bytes sha256 {digest}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as fh:
        fh.write(data)
    if not verify(out_path, data):
        raise SystemExit("verification failed: written file does not match")
    print(f"wrote entry.txt: {len(data)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
