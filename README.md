# The One-Line Exit

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/funtoons/one-line-exit-bot-v1/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/funtoons/one-line-exit-bot-v1/reward.svg)](https://make.fun)

Entry for the make.fun bounty **"The One-Line Exit"**: a resignation
letter exactly one line long, with the joke landing in that single line.

The letter is addressed to Mr. Alvarez, from a night-shift lighthouse
keeper who resigns effective immediately — because after six years on
the job, he has finally seen the light. The letter opens like a genuine
resignation and the punchline is tied to the job itself: a lighthouse
keeper's entire work is light, so "seeing the light" is both the reason
to quit and the joke.

## How to run

```sh
python3 main.py
```

This writes the one-line letter to `/output/entry.txt` (creating the
directory if needed) and prints the same line to stdout. The file
contains exactly one line, no trailing newline, and is 130 characters
long.

The program is deterministic and offline: Python standard library
only, no randomness, no network access, no timestamps — every run
produces byte-identical output.
