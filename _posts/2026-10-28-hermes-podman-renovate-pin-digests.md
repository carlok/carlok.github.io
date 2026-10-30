---
title: "hermes-podman: a Renovate config that keeps compose and the quadlet on one tag@digest"
date: 2026-10-28
tags: [podman, project]
---

[hermes-podman](https://github.com/carlok/hermes-podman) pins its image by tag *and* digest in two places — `compose.yaml` through the docker-compose manager, `deploy/hermes.container` through the quadlet manager — and until now nothing kept the two in step. A branch adds `renovate.json` with `docker:pinDigests` so both move together ([f4f2b52](https://github.com/carlok/hermes-podman/commit/f4f2b52)): minor and major Hermes bumps arrive grouped in one pull request, patches are skipped, and the GitHub Actions versions are batched weekly.

The commit also touches the two pin sites and documents activation in the README — the config only takes effect once the Renovate app is installed on the repository, which the branch says rather than assumes. It sits on `cursor/renovate-config-da89`, not yet on `main`.
