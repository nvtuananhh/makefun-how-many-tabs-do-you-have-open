"""How Many Tabs Do You Have Open? — one honest tab count.

The program writes a single number to /output/entry.txt: the
honest count of browser tabs open right now.
"""

import os

MAX_CHARS = 5
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The count is the confession: 137. Far above what the field
# would guess, yet a number a real tab hoarder could honestly
# have open — specific and odd, so it reads as measured, not
# picked to shock. No round number, no joke number: a prime
# that hints at a life of tabs opened and never closed.
COUNT = "137"


def build_count():
    """Return the entry count, checked: digits only, 1-5 characters."""
    count = COUNT.strip()
    assert count.isdigit(), "entry must be digits only"
    assert 1 <= len(count) <= MAX_CHARS, "entry must be 1-5 characters"
    return count


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(count, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(count + "\n")
    return path


def main():
    count = build_count()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(count)


if __name__ == "__main__":
    main()
