---
title: "caciarabot: a Distroless runtime halves the image, and CI now runs the config validator"
date: 2026-10-29
tags: [bot, podman]
---

[caciarabot](https://github.com/carlok/caciarabot)'s production stage moved from `python:3.12-slim` to `gcr.io/distroless/python3-debian12:nonroot` ([#8](https://github.com/carlok/caciarabot/pull/8), [2bfc4e2](https://github.com/carlok/caciarabot/commit/2bfc4e2)): no shell, no package manager, no curl, entrypoint still the exec-form `python -m caciarabot.main`, running as UID 65532 with `/data` prepared and owned in a slim `runtime-prep` stage. The built image drops from 213 MB to 114 MB.

The venv is built on `python:3.11-slim-bookworm` with `/usr/bin/python3` symlinks so the interpreter resolves inside Debian 12's distroless Python, while dev and CI stay on 3.12 — `requires-python` is `>=3.11` and the tests cover both — and the `dev` target is pinned to `3.12-slim-bookworm` so it cannot drift to Trixie. Distroless bases from `dhi.io` were tried first and refused anonymous pulls, so the public `gcr.io` image stands in as a drop-in alternative.

The same week closed a gap the README had been asking operators to cover by hand: `uv run --frozen caciarabot-validate` now runs in CI between Ruff and pytest ([#7](https://github.com/carlok/caciarabot/pull/7), [99bd603](https://github.com/carlok/caciarabot/commit/99bd603)), one workflow line over 207 passing tests.
