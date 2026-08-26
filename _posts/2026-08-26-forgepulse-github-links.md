---
title: "forgepulse: GitHub links on detail pages, gghstats issues checked"
date: 2026-08-26
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse)'s repository detail page now
links its title, top referrers, and popular paths straight to GitHub (paths
always, referrers only when they look like real hostnames), and the JSONL
export filename embeds a UTC timestamp so re-downloads stop silently
overwriting the previous file. A cross-check against the issues opened on
hrodrig/gghstats found that three of them applied to forgepulse too — the
export filename, the stats-panel jargon, and the rank column header — and
were fixed here; the locale-formatting issue does not apply in the same shape
yet.
