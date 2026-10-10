---
title: "deck-lovers: the projector disconnect survives cancellation, and the deploy script reads .env"
date: 2026-10-09
tags: [tool, security]
---

[deck-lovers](https://github.com/carlok/deck-lovers)' `/ws` disconnect cleanup
ran unshielded, so a cancelled task could skip telling the audience the
projector had left and leave stale clients behind — Starlette's `TestClient`
cancels the app task right after sending the disconnect, which made the
websocket tests hang about four runs in ten. The cleanup is now wrapped in a
shielded anyio cancel scope, two test races are gone, and a regression test
cancels the handler the way the client does
([3c4e938](https://github.com/carlok/deck-lovers/commit/3c4e938)).

Following the deploy preflight added earlier, `deploy.sh` now reads `PORT`,
`PALETTE`, `FONT`, `EMOJI`, `LOGO`, `FRAME`, `LOGO_ON`, `PDF_MODE`, `PDF_NAME`
and `PDF_QUALITY` from `.env` with flag-over-environment-over-file precedence,
parsing the file rather than sourcing it; a local `--pdf-only` run writes only
the named PDF and leaves `output/audience.pdf` alone. The port check, the `.env`
loader and the `audience.pdf` copy are covered by a new
`tests/deploy_test.sh` that runs in CI
([e45374b](https://github.com/carlok/deck-lovers/commit/e45374b)).
