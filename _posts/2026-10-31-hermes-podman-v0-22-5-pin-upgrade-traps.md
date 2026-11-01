---
title: "hermes-podman: pinned to Hermes v0.22.5, and the three things that make a healthy upgrade look broken"
date: 2026-10-31
tags: [podman, project]
---

[hermes-podman](https://github.com/carlok/hermes-podman) now pins `docker.io/nousresearch/hermes-agent` at `v0.22.5@sha256:9c5561579f3f…` in `compose.yaml` and in the quadlet `deploy/hermes.container` together, one commit for both sites, with the digest taken from the Docker Hub tag record rather than typed ([8c044e1](https://github.com/carlok/hermes-podman/commit/8c044e1)). The jump is from v0.21.6, so it crosses the release boundary where `docs/UPGRADE.md` had nothing to say.

That gap is now filled ([b35e4c0](https://github.com/carlok/hermes-podman/commit/b35e4c0)): a repo-first pin-bump flow — resolve the digest, commit both files with the tag, digest and publish date, then `make backup && git pull --ff-only && make down && make up && make verify`, so rollback is a `git revert` of one commit — and a post-upgrade checklist that deliberately does not gate on log greps. From v0.22 the messaging connect line is logged through the logger into `data/logs/` instead of container stdout, so `podman logs` can look silent seconds after a healthy connect; the checklist asks `hermes --version`, `_config_version`, `gateway status`, `cron list` and `memory status` instead. A `gateway.exit_nonzero` line in `data/logs/gateway-exit-diag.log` is usually the teardown of a rollback rather than a crash, and is to be read against `container-boot.log` first.

The v0.21 → v0.22 notes are the part worth keeping: config migrates on first start (`_config_version` 50 → 51) on Python 3.14.9 instead of 3.14.7, `session_reset`'s idle and daily modes are retired and want `hermes config unset session_reset`, and the memory providers left core — a profile still naming one boots with "could not be installed automatically" and needs `hermes plugins install holographic --yes-deps --enable`, since without `--yes-deps` a non-interactive install refuses and installs nothing.
