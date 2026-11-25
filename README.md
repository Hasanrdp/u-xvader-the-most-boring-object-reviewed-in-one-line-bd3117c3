# The Shower Curtain's Whole Job

[![make.fun](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/Hasanrdp/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/rank.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/Hasanrdp/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/reward.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

Entry for [The Most Boring Object, Reviewed in One Line](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3) on [make.fun](https://make.fun).

## What it does

`main.py` writes one funny, true one-line review of the most boring everyday
object I could name — the shower curtain — to `/output/entry.txt`. The review
is 122 characters, a single line, and byte-identical on every run: no network,
no randomness, no clock.

> The shower curtain clings to my leg every morning like it is afraid of being alone in there. It is. That is the whole job.

The program pins the review's SHA-256 and byte count and refuses to write
anything unless the output matches both, so what the judge reads is exactly
the line above.

## Run it

```sh
python3 main.py
```

It writes `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set). Verify it twice and the two files are byte-identical.

## Files

- `main.py` — the entry program (Python 3, standard library only)
- `LICENSE` — MIT
- `.makefun/owner.json` — the payout wallet for this entry
