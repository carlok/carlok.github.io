---
title: "topshift-trend: a trending description in CJK or Cyrillic no longer takes a slot the bot was going to announce"
date: 2026-11-27
tags: [bot, telegram]
---

[topshift-trend](https://github.com/carlok/topshift-trend) announced whatever GitHub's trending list put in its first few rows, and when some of those descriptions were not English the bot spent its slots on entries it could not report usefully. `ENGLISH_ONLY` now filters them by default, and the fetch walks further down the list until `TOP_N` English-capable entries are filled, so the same number of repositories reaches the chat ([#14](https://github.com/carlok/topshift-trend/pull/14), [2ee3e88](https://github.com/carlok/topshift-trend/commit/2ee3e88)).

The detection has no dependency behind it: letters outside the Basic and Extended Latin blocks above a 15 % threshold mark a description as non-English, which covers CJK, Cyrillic and Arabic without a language model. The setting is documented in the README and `.env.example`, `ENGLISH_ONLY=false` restores the old first-`TOP_N` behaviour, and the suite that went with it runs 52 tests at 94.32 % coverage.
