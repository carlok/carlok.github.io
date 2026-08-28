---
title: "caciarabot: config example file and mood-range daily thoughts"
date: 2026-08-28
tags: [bot, telegram]
---

[caciarabot](https://github.com/carlok/caciarabot) stopped tracking its live
config: the working `bot.jsonc` is no longer in the repo, and a
`bot.jsonc.example` ships instead, so local state can't be clobbered by updates
or leak into history. The daily thought generator also gained a real mood range
and occasionally follows a Wikipedia rabbit hole instead of picking a templated
topic.
