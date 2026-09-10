---
title: "topshift-trend: a cooldown so a chat is not notified twice about the same repo"
date: 2026-09-10
tags: [telegram, bot, tool]
---

[topshift-trend](https://github.com/carlok/topshift-trend), the Telegram bot
that watches GitHub's monthly trending list, learned to
[suppress repositories it recently notified](https://github.com/carlok/topshift-trend/commit/34f3aec):
a repo that drops out of the top-N and comes back used to announce itself to
every subscriber again. The bot now keeps a `notification_history.json`
alongside its state and subscribers, and the scheduled check filters out keys
seen inside a configurable window — `NOTIFICATION_COOLDOWN_DAYS`, default 30
days, `0` disables the suppression. The commit touches the config, store and
main loop plus three test files, and the check's log line now reports how many
entries were suppressed next to how many notifications actually went out.
