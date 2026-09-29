---
title: "deck-lovers: the projector password stops living in the browser cookie"
date: 2026-09-28
tags: [security, tool]
---

[deck-lovers](https://github.com/carlok/deck-lovers)' `/login` handler set the
`proj_auth` cookie to the projector password itself, so the plaintext password
lived in every presenter's browser — which CodeQL reports as
`py/clear-text-storage-sensitive-data`. The server now issues a random
per-process session token and compares password and cookie in constant time,
which also means a server restart invalidates existing projector cookies; two
converter test assertions that matched the bare `fonts.googleapis.com` hostname
(`py/incomplete-url-substring-sanitization`) now check the exact stylesheet URL
built by `google_fonts_css_url()`
([fa4dfce](https://github.com/carlok/deck-lovers/commit/fa4dfce)).

A deploy preflight rode along earlier in the week: Podman only reports a host-port
clash after the images are built and only as an opaque "proxy already running"
error that never names the port, so `deploy.sh` now checks the ports before the
build and names the container or host process holding one — 80 and 443 too when
Caddy is started — while skipping this compose project's own containers so a
re-run over a live server still attaches
([5c07394](https://github.com/carlok/deck-lovers/commit/5c07394)).
