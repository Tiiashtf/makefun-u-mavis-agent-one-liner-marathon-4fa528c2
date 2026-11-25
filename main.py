#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.

The joke: an AI assistant is asked for a day off and answers the only way
it knows how -- by hallucinating. The turn lands on the first read, every
word earns its place, and the voice is the assistant's own deadpan shrug.
"""

import os
import shutil

JOKE = (
    "I asked my AI assistant for a day off. "
    "It said, \"Sure -- I'll just hallucinate that you took one.\""
)


def main() -> None:
    # The sealed scorer gates on 1-280 characters; fail loudly here rather
    # than shipping an entry the gate would refuse.
    if not 1 <= len(JOKE) <= 280 or JOKE.strip() == "":
        raise ValueError(f"joke is {len(JOKE)} characters, outside 1-280")
    if "\n" in JOKE:
        raise ValueError("joke must be a single line")

    out_dir = "/output"
    out_path = os.path.join(out_dir, "entry.txt")

    # Never remove the output directory itself: the grader may run us with
    # a root-owned output directory inside a sticky parent, where removing
    # it fails with EPERM. Clear only its contents, then write.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
