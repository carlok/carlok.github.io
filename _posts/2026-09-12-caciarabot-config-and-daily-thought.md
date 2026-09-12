---
title: "caciarabot: settings out of the repo, and a daily thought that can lose the model"
date: 2026-09-12
tags: [bot, telegram]
---

[caciarabot](https://github.com/carlok/caciarabot) no longer has a tracked
config file at all: every field of the bot config now has a default in code
and a `CACIARABOT_<FIELD_NAME>` environment override, `.env` is the only
per-deployment file, and an unrecognised `CACIARABOT_*` variable is a startup
error naming the variable instead of a silent no-op
([64d70f5](https://github.com/carlok/caciarabot/commit/64d70f5)) — the old
`config/bot.jsonc` had aborted two live updates, which is why it was deleted
rather than relocated, with a stdlib-only `deploy/bot_jsonc_to_env.py` left to
convert an existing one on the deployment host. The daily thought gained a
diction dimension rotating orthogonally to mood and depth — concrete, spoken,
technical, plain, 224 combinations — after sampling 42 real generations showed
all 14 moods collapsing into the same elegiac dust-motes-in-a-sunbeam register
([bb2666c](https://github.com/carlok/caciarabot/commit/bb2666c)). It also
gained a deterministic local fallback for the day the one API call fails
([548e2d6](https://github.com/carlok/caciarabot/commit/548e2d6)): 30
hand-written openers and 12 closings under `config/fallback/`, drawn through
the same no-repeat history as the prompts, because a free-tier 429 is a spent
quota and retrying spends more of the scarce thing.
