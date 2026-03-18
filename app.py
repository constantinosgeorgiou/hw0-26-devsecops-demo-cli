#!/usr/bin/env python3

import argparse
import hashlib
from pathlib import Path

import requests


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="hw0 devsecops demo CLI (constantinosgeorgiou)"
    )
    parser.add_argument("--quote", action="store_true", help="Print a static quote.")
    parser.add_argument(
        "--hash",
        metavar="TEXT_OR_PATH",
        help="If this looks like a path, hash the file; otherwise hash the given text.",
    )
    parser.add_argument(
        "--fetch",
        metavar="URL",
        help="Fetch a URL (best-effort) and print its length. Not used by CI.",
    )
    args = parser.parse_args()

    if args.quote:
        print("Constantinos Georgiou says: security is a habit.")
        return 0

    if args.hash:
        maybe_path = Path(args.hash)
        if maybe_path.exists():
            print(sha256_file(maybe_path))
        else:
            print(sha256_text(args.hash))
        return 0

    if args.fetch:
        resp = requests.get(args.fetch, timeout=5)
        print(f"fetched {len(resp.content)} bytes")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
