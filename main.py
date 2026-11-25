"""Entry generator for "The Funniest Office Joke" (variant A).

Writes the 119-char printer joke to /output/entry.txt (the path the
grader reads), with a best-effort copy to the repo root for local runs.
Output is byte-stable by design: the text is a single frozen constant.
"""
import os

JOKE = "The office printer jammed on deadline day, so I called IT, and IT wrote back: the printer reported you for abuse first."

TEXT = JOKE + "\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Self-check: the written output must be exactly the frozen text.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == TEXT, "entry.txt does not match frozen TEXT"
    # Best-effort copy to the repo root. The grader sandbox mounts the
    # repo read-only, so this must never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
