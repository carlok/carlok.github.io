---
title: "topshift-trend: a repository that drops off the trending list for a few days is not a new arrival when it comes back"
date: 2026-11-15
tags: [bot, telegram]
---

The cooldown in [topshift-trend](https://github.com/carlok/topshift-trend) was the weak part of the announcement rule: a repository that stays on GitHub's monthly trending list and then disappears for a couple of days could be read as entering the list again when it returned, so the bot announced a project it had already announced. The fix refreshes the notification cooldown from the last saved baseline rather than from the moment of the announcement, which keeps a short absence quiet ([3502ce4](https://github.com/carlok/topshift-trend/commit/3502ce4), merged [86eff9a](https://github.com/carlok/topshift-trend/commit/86eff9a)).
