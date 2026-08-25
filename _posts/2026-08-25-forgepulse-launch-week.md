---
title: "forgepulse: launch-week fixes and features"
date: 2026-08-25
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse) got its launch-week pass: the
repository table is paginated, a favicon landed, and the static "LOCAL" badge
now shows the running git ref. On the ops side, a scheduled sync that was
silently failing (the /data volume was never chowned to the app user) and a
repository detail page that replayed every historical referrer day are fixed,
and the production container now restarts itself after a crash or reboot.
