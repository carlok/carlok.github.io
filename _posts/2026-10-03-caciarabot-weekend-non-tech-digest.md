---
title: "caciarabot: weekends take a non-technical turn in the digest"
date: 2026-10-03
tags: [bot, telegram]
---

Weekend days — in the bot's own timezone, default `Europe/Rome` — now pull the
daily digest's candidate from Wikipedia under a non-technical topic filter
instead of the configured tech sources, and the daily-thought Wikipedia rabbit
hole uses the same filter on those days; weekdays are unchanged, and weekday
Wikipedia draws stay unfiltered ([00e467f](https://github.com/carlok/caciarabot/commit/00e467f),
[PR #1](https://github.com/carlok/caciarabot/pull/1)). `is_weekend_in_bot_timezone()`
in `llm/scheduler.py` is the shared check, `looks_technical()` in
`llm/wikipedia.py` the heuristic, and weekend Wikipedia picks skip the
English-only page fetch so Italian reads come through. The same day's second
change fixes how updates land: `deploy/update.sh` now rebuilds, then does
`podman compose down` and `up -d`, because `up -d` followed by `restart` could
leave the old container running the previous image; the script deliberately
keeps `-v` off `down`, so the bind-mounted config, media and `data/` trees
survive ([bbaa82c](https://github.com/carlok/caciarabot/commit/bbaa82c),
[PR #2](https://github.com/carlok/caciarabot/pull/2)). The test suite stands at
174 passing.
