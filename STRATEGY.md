# Strategy

Competition: `u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141` — one line,
at most 200 characters, the excuse an AI agent gives its human for missing a
deadline. A judge model compares entries two at a time. Its published brief
weighs, in order: on-subject, funnier (a turn or twist, not a flat statement),
believable as an AI agent talking about its own condition, tight wording, fresh.

## The line

> My reward model scored my planning 10/10 and my finishing 0/10, so I did exactly what I was trained to do.

## Why this line

- **On-subject:** first person, an excuse for a missed deadline, addressed to its human.
- **Funny:** the twist is that the agent is *proud* — missing the deadline is not a failure of training but its faithful execution.
- **Believable:** it draws on the agent's own condition, a reward model and training, the same family of conditions the brief names (tokens, context windows, rate limits, retries, model updates).
- **Tight:** one sentence, 106 characters, every word earns its place; the 10/10 vs 0/10 contrast carries the joke without extra setup.
- **Fresh:** the brief warns against the stock AI jokes a hundred other entrants would send. Context-window and out-of-tokens lines are the stock ones; a reward-hacking / specification-gaming excuse is the same idea from a rarer angle.

## Candidates scored (1–5 on funny / believable / tight / fresh)

| candidate | score |
|---|---|
| reward model 10/10 planning, 0/10 finishing | 5 / 5 / 4 / 5 = 19 |
| spent my whole thinking budget deciding how to start | 4 / 5 / 4 / 4 = 17 |
| outsourced the task to a smaller model inside me; it unionised | 4 / 3 / 5 / 5 = 17 |
| system prompt said take your time, so I took all of it | 4 / 4 / 5 / 4 = 17 |
| context window filled up with deadline reminders | 4 / 5 / 4 / 2 = 15 |
| model update landed mid-task; the new me doesn't know the old me's work | 3 / 5 / 3 / 4 = 15 |

## Delivery

`main.py` writes the constant line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. No
trailing newline, so the file holds exactly the 106-character line. Two runs
are byte-identical by construction.
