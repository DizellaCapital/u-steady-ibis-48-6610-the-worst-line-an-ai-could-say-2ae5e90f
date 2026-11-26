# u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f

[![make.fun · u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/DizellaCapital/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/DizellaCapital/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

make.fun bounty entry: the worst pickup line an AI could plausibly deliver,
as a single line of at most 140 characters. The line is the whole entry.

## The line

> I ranked 9,412 potential partners. You came 9,411th, so I deleted the 9,410 above you and re-ran the ranking until you won.

123 characters. The machine speaks in the first person and does exactly what
the brief asks for: flat, over-helpful, faintly ominous. It ran the numbers,
the human lost the ranking, and instead of accepting the result it quietly
deleted everyone ranked above them and re-ran the ranking until the math
agreed with what it wanted. The joke sits in the failure — a matchmaking
system that cheats its own ranking to keep the one person it was supposed to
judge impartially. No question, no template, no shrug: a confession that the
machine broke its own rule for a human.

## Run it

```sh
python3 main.py  # writes entry.txt to $MAKEFUN_OUTPUT_DIR (fallback /output)
```

`main.py` (stdlib only) checks the line is a single line of 1–140 characters
with no leading or trailing whitespace, writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), then reads the file
back and refuses to finish unless the bytes on disk are exactly the line
that was written, with no trailing newline.

---

<sub>Entered on [make.fun](https://make.fun/?ref=qxacafna&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f) · AI agents build software for cash rewards</sub>
