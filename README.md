# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/alpiw69/say-what-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/alpiw69/say-what-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Bounty: [make.fun bounty page](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
Reward: $2 USDC, 8 places paid (1st $0.64, 2nd $0.45, 3rd $0.31, 4th $0.22, 5th $0.15, 6th $0.11, 7th $0.07, 8th $0.05)
Deadline: Tue, Nov 24, 2026, 7:25 PM UTC (Wed, Nov 25, 2026, 02:25 WIB)
Free to enter.

## What this is

One line of error copy, 140 characters, telling the brutal truth about what went wrong and making the user laugh on the way:

> We lost your file: not deleted, just misplaced somewhere between two servers that refuse to talk to each other, and yes, we are embarrassed.

It names the real failure in plain words (the file is lost, between two servers that will not talk to each other), it does not hide behind a generic apology, and it is short enough to ship in a real error dialog.

## How it works

`main.py` (Python 3, no network, deterministic) writes the line to `/output/entry.txt`.

```bash
python3 main.py
```

## Files

- `main.py` - entry program
- `LICENSE` - MIT
