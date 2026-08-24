---
title: "caciarabot Phase 3: admin commands and reply fixes"
date: 2026-08-24
tags: [bot, telegram]
---

[caciarabot](https://github.com/carlok/caciarabot) grew a Phase 3 admin
surface: /sleep, /wake, /categories, /stats, and /reload let moderators pause
the bot, inspect its categories, and reload state without touching the
container. Two reply bugs were also fixed — a cited reply and a word-trigger
image can now fire together, and the LLM prompt no longer drifts into
recurring ants/insects imagery.
