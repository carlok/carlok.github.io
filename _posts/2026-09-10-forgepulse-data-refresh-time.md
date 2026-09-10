---
title: "forgepulse: the dashboard now shows when its numbers were last refreshed"
date: 2026-09-10
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse) shows the age of its own data:
the homepage now reads the most recent successful sync run — already recorded in
the `sync_runs` table but never surfaced — and renders it next to the git-ref
pill as `Updated <UTC> · <local> (Xh Ym ago)`, ticking every minute
([d4c5e85](https://github.com/carlok/forgepulse/commit/d4c5e85)). Traffic
history is only as useful as the moment it was collected, and until now the
dashboard gave no way to tell a stale snapshot from a fresh one. The change
touches two new frontend modules plus tests for the relative-time formatter and
the API field behind it.
