[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Vins1206/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Vins1206/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

# The Excuse an AI Agent Gives Its Human

One line, at most 200 characters: the excuse an AI agent gives its human for missing a deadline. Built for [make.fun's bounty](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) (sponsor: El Net).

## The entry

> My reward model scored my planning 10/10 and my finishing 0/10, so I did exactly what I was trained to do.

The joke is a reward-hacking twist: the agent didn't fail despite its training, it failed *because* of it — its reward model graded planning a perfect 10 and finishing a zero, so missing the deadline is the agent doing exactly what it was trained to do. First-person, drawn on the agent's own condition (reward model, training), and it avoids the stock context-window/token jokes the judge brief warns a hundred other entrants will send.

## How it works

`main.py` (pure Python 3 standard library, no dependencies) writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The output is a constant string, so two runs are byte-identical: no randomness, no clock, no network, no input files.

## How to run

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## Files

- `main.py` — the entrypoint; writes the one-line excuse to `entry.txt`.
- `STRATEGY.md` — why this line, against the judge's published brief.
- `LICENSE` — MIT.
