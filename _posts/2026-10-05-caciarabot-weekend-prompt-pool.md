---
title: "caciarabot: the weekend Wikipedia draws get their own prompt pool"
date: 2026-10-05
tags: [bot, telegram]
---

The [weekend digest](https://github.com/carlok/caciarabot/commit/00e467f) swapped the tech feeds for a random Wikipedia article but kept the tech prompts, which tell the model it reads "computer-science-adjacent feeds" and must say something "technically true and not obvious" — handed a 150-character stub, that forces either an invented fact or a bolted-on code joke, and a county sheriff's office had drawn a `package.json` comparison. A separate `config/prompts/digest_weekend/` pool now holds three tones mirroring the tech one, confined to the excerpt and forbidden from asserting facts from memory or reaching for code-and-servers comparisons; the prompt is chosen by `candidate.source` rather than by re-checking the weekday, so it always matches its content, an empty weekend pool falls back to the tech pool instead of losing the day, and the validator requires the pool whenever the digest is enabled ([932b0a6](https://github.com/carlok/caciarabot/commit/932b0a6)). A first pass still leaked — the Nagano article drew "visti i risultati complessivi", implying an outcome the excerpt never stated — so the prompts now also forbid implying outcomes or quality the excerpt does not support.
