---
title: "deck-lovers: the deploy script checks host ports before it builds"
date: 2026-09-22
tags: [podman, tool]
---

Podman only reports a host-port clash after the images are built, and only as
an opaque "proxy already running" error that never names the port. The deploy
script in [deck-lovers](https://github.com/carlok/deck-lovers) now runs a
pre-flight check in local serve mode before the build, naming the container or
host process that is actually holding the port — 80 and 443 included when Caddy
is started — while skipping this compose project's own containers, so re-running
over a live deck-lovers server still attaches instead of failing
([5c07394](https://github.com/carlok/deck-lovers/commit/5c07394)).
