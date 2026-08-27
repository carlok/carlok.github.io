---
title: "forgepulse: routing and link-click fixes"
date: 2026-08-27
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse) fixed two web-UI bugs:
opening a repository detail page directly, or in a new tab, no longer 404s,
and modifier-clicking a link now opens it in a new tab instead of swallowing
the click. CI was retriggered after a GitHub Actions outage stalled the
pipeline.
