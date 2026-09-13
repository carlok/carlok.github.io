---
title: "forgepulse: manual refresh and an on-demand sync, behind a single-flight guard"
date: 2026-09-13
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse) grew the two controls its
dashboard was missing: **Refresh** re-fetches the stored dashboard and detail
data without touching GitHub at all, while **Sync now** performs a real pull
through the existing `POST /api/v1/sync` endpoint outside the hourly schedule
and now surfaces the server's error inline — an expired token says so
immediately instead of failing silently until the next scheduled attempt
([87cfe54](https://github.com/carlok/forgepulse/commit/87cfe54)). On-demand
sync then exposed a contention bug worth fixing properly: the scheduled tick and
the new endpoint shared one GitHub collector with no coordination, so a click
landing during the hourly run let multiple full 84-repo syncs proceed at once,
each with its own bounded per-repo fetch — enough load to trip secondary rate
limiting and queue on SQLite's single writer, turning overlap into a crawl
rather than an error. A single-flight guard now rejects the second sync instead
of letting the two contend
([47b2e73](https://github.com/carlok/forgepulse/commit/47b2e73)).
