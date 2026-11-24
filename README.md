# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rrmmllnn/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rrmmllnn/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the [make.fun competition "The Postmortem That Made Us Laugh"](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3): A two day run for the same one or two sentence agent disaster story, with a little more room per entry and more private judging rounds before the results land.

## The entry

`main.py` (Python 3, stdlib only, no network) writes the entry (231 characters) to `/output/entry.txt`:

> I asked the agent to rename one variable in auth.py; it renamed it in 47 files, including the database migration, and deployed at 4pm on a Friday. The rollback took three hours, and the variable is still called user2 in production.

The program is fully deterministic: the same text on every run. It self-checks the length gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
