---
title: "caciarabot: the running bot now says which settings it loaded, and /stats shows what actually fired"
date: 2026-11-04
tags: [bot, telegram]
---

The complaint was that `CACIARABOT_LLM_REPLY_PROBABILITY=0.05` still replies too often, and the roll turned out to be correct — 5.01% over 200,000 simulated messages, one roll per message, no second handler — which left the value the running process actually holds as the suspect. That is hard to inspect in [caciarabot](https://github.com/carlok/caciarabot) now that production runs Distroless: no shell, no `printenv`. A `.env` edit followed by `podman compose restart` also keeps the old value, because restart does not re-read `env_file`; only `down` then `up -d` does, which `deploy/update.sh` already does ([729dedc](https://github.com/carlok/caciarabot/commit/729dedc)).

So `main.py` logs a `settings_loaded` line at startup with the ambient-behaviour settings it really read — no secrets — and `podman compose logs | grep settings_loaded` answers the question directly. `/stats` had the counters but showed none of them; it now reports spontaneous replies, replies when addressed and emoji reactions as a count and as a percentage of observed messages, so "too frequent" becomes a number to compare against the configured probability. The emoji line is the one that explains the complaint: at the migrated default of 0.33 it fires on one message in three, which reads far more like "it replies" than a 5% text reply does.

Both locales gained the three strings with their key sets verified identical, and a new `tests/test_stats_command.py` covers the command.
