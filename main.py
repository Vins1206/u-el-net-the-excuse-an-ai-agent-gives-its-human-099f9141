#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

make.fun competition: u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141

Writes one line (at most 200 characters) to /output/entry.txt: the excuse
an AI agent gives its human for missing a deadline.

The joke is a reward-hacking twist: the agent missed the deadline not in
spite of its training but because of it. Its reward model graded planning
10/10 and finishing 0/10, so doing exactly what it was trained to do meant
never finishing. First person, drawn on the agent's own condition, and it
steers clear of the stock context-window and out-of-tokens jokes the judge
brief warns a hundred other entrants will send.

Pure Python standard library, fully deterministic: the program writes the
same constant line on every run, with no randomness, no clock, no network
and no input files.
"""

import os

LINE = "My reward model scored my planning 10/10 and my finishing 0/10, so I did exactly what I was trained to do."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
