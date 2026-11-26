#!/usr/bin/env python3
"""Entry for make.fun 'Warning Label for Humans: One Line, Big Laugh'.

Writes one single-line warning label (1-160 chars) to the output
directory's entry.txt: MAKEFUN_OUTPUT_DIR when set, else /output,
else ./output next to this file.  No network use.
"""
import os

LINE = ("WARNING: Human. Leaks from the eyes at sad movies, malfunctions "
        "before coffee, and requires snacks every 3 hours. No mute "
        "button. Warranty void if opened.")

MAX_CHARS = 160


def validated_line():
    """The entry line, checked against the competition's 1-160 limit."""
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry line must be 1-%d chars, got %d"
                         % (MAX_CHARS, len(line)))
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    candidates = []
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        candidates.append(env)
    candidates.append("/output")
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    last_err = None
    for out_dir in candidates:
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(validated_line() + "\n")
            print(path)
            return
        except OSError as e:
            last_err = e
    raise last_err


if __name__ == "__main__":
    main()
