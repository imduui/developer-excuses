#!/usr/bin/env python3
"""Write one funny developer excuse to /output/entry.txt.

The line: every test passed because there were no tests at all --
the test file has been sitting in .gitignore since 2023.
"""
import os

LINE = "All the tests passed \u2014 all zero of them. The test file's been in .gitignore since 2023."


def main():
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
