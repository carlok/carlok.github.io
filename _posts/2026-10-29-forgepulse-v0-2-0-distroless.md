---
title: "forgepulse v0.2.0 moves production to Distroless, adds a built-in healthcheck, and prints its own version"
date: 2026-10-29
tags: [rust, project]
---

[forgepulse](https://github.com/carlok/forgepulse) released
[v0.2.0](https://github.com/carlok/forgepulse/releases/tag/v0.2.0) on 28 October
([34d03d2](https://github.com/carlok/forgepulse/commit/34d03d2)). The production
image is now `gcr.io/distroless/cc-debian12:nonroot` with a built-in
`forgepulse-server healthcheck` instead of a shell-less Alpine base, and the
README gained the section the move needs: an existing data volume must be
`chown`ed to uid 65532 once, before the container will read it
([#8](https://github.com/carlok/forgepulse/pull/8), [c97d705](https://github.com/carlok/forgepulse/commit/c97d705),
[256f853](https://github.com/carlok/forgepulse/commit/256f853)). The header
now shows what is running — `v0.2.0 · main@abc1234` — and `/api/health`
reports the same pair, so a stale deploy is visible without reading the image
digest.

The same release added `scripts/deploy.sh` for a one-command local build and
deploy, and made overlapping syncs get rejected rather than contend for the
SQLite writer.
