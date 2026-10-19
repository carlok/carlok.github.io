---
title: "forgepulse: human attention v2 scores every repo from fresh inputs"
date: 2026-10-18
tags: [rust, tool]
---

[forgepulse](https://github.com/carlok/forgepulse)'s human-attention score had three ways of lying. Empty referrer lists were read as unknown rather than as zero, so 55% of repos scored N/A; referrer snapshots never expired, and a 53-day-old one still ranked fifth on the chart; and repos under 30 days old had no star or fork baseline at all, so the newest projects were scored against nothing ([affe833](https://github.com/carlok/forgepulse/commit/affe833)).

The v2 score fixes all three in the inputs rather than in the formula: referrers now come from a snapshot at most a day old or count as zero, and a missing baseline falls back to the latest earlier row, to zero for repos created inside the window, or to the first observation. Two smaller corrections come with it — a fork now weighs the same as a star, and a zero score is ranked as unranked and shown as a dash instead of disappearing into a wide tie — plus trend markers for entering and leaving the chart.
