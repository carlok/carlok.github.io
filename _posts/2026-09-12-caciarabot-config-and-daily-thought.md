---
title: "caciarabot's daily thought: a diction dimension, and a fallback for the day the model is gone"
date: 2026-09-12
tags: [bot, telegram]
---

[caciarabot](https://github.com/carlok/caciarabot)'s daily thought generator
gained a diction dimension rotating orthogonally to mood and depth — concrete,
spoken, technical, plain, 224 combinations — after sampling 42 real generations
showed all 14 moods collapsing into the same elegiac dust-motes-in-a-sunbeam
register ([bb2666c](https://github.com/carlok/caciarabot/commit/bb2666c)). It
also gained a deterministic local fallback for the day that one API call fails
([548e2d6](https://github.com/carlok/caciarabot/commit/548e2d6)): 30
hand-written openers and 12 closings under `config/fallback/`, drawn through the
same no-repeat history as the prompts, because a free-tier 429 is a spent quota
and retrying spends more of the scarce thing. The settings themselves — which had
already [left the repository](/blog/2026/08/28/caciarabot-config-mood/) — now
live entirely in the environment: every field defaults in code,
`CACIARABOT_<FIELD_NAME>` overrides it, and an unrecognised `CACIARABOT_*`
variable is a startup error naming the variable instead of a silent no-op
([64d70f5](https://github.com/carlok/caciarabot/commit/64d70f5)), with a
stdlib-only `deploy/bot_jsonc_to_env.py` left behind to convert an existing
`config/bot.jsonc` on the deployment host.
