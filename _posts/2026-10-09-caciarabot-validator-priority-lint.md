---
title: "caciarabot: telegram-shaped photo validation, enforced rule priority, and a lint-found dangling task"
date: 2026-10-09
tags: [bot, telegram]
---

[caciarabot](https://github.com/carlok/caciarabot)'s validator already caught a
file over Telegram's upload ceiling, but size is not the only way Telegram
refuses a photo: width and height above 10000 px, or a longer side more than 20×
the shorter, fails with `PHOTO_INVALID_DIMENSIONS` even at a few hundred KB —
and a panorama or tall screenshot is exactly the file people drop in. A new
`telegram/imagesize.py` reads the dimensions out of the header with the standard
library alone — PNG (IHDR), JPEG (skip the `APPn` segments to the
start-of-frame marker) and all three WebP variants — checked against macOS
`sips` on all 142 real images in `media/` with no false positives
([b06e315](https://github.com/carlok/caciarabot/commit/b06e315)).

`priority` was parsed, accepted by the schema, and never read by
`decision.select`, so a rule author could set it and nothing happened; selection
now stable-sorts the firing rules by priority after the shuffle, with a
high-priority rule that loses its probability roll stepping aside rather than
silencing lower ones ([c32563c](https://github.com/carlok/caciarabot/commit/c32563c)).
Adding ruff to CI (with `RUF006`) found the daily-thought and digest loops
started with a bare `asyncio.create_task()` holding no reference — asyncio keeps
tasks only weakly, so such a task can be garbage-collected mid-run, and anything
escaping the loop ended it silently with the bot never posting again
([62c3302](https://github.com/carlok/caciarabot/commit/62c3302)). The digest no
longer discards the day when generation fails: `config/fallback/digest.txt`
holds twelve canned comments that rotate through the existing no-repeat
machinery and say nothing about a link the bot never read, with no retry, since
a 429 means the quota is gone
([67887df](https://github.com/carlok/caciarabot/commit/67887df)).
