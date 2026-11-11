---
title: "matrix-podman-stack: podman-compose 1.5 puts the stack in a pod that keep-id cannot live in"
date: 2026-11-10
tags: [podman, tool]
---

GitHub's runners moved from `podman-compose` 1.0.6 to 1.5.0 and [matrix-podman-stack](https://github.com/carlok/matrix-podman-stack) stopped integrating: the scheduled run on 9 November and two Dependabot PRs failed, because 1.5 ignores `COMPOSE_PROFILES` and starts profiled services only through `--profile`. `scripts/compose_stack.sh` and the integration helper now pass `--profile` when the binary advertises the flag, and the systemd user unit starts and stops through that script ([#41](https://github.com/carlok/matrix-podman-stack/pull/41), [eaf301b](https://github.com/carlok/matrix-podman-stack/commit/eaf301b)).

The second change is the one that would have taken the stack down: 1.5 creates a project pod by default, and podman refuses `userns_mode: keep-id` together with a pod — `--userns and --pod cannot be set together` — which stopped Synapse, the bootstrap step and Prometheus, so `compose.yaml` sets `x-podman.in_pod: false` for the 1.0.x default, and a 1.5 dry run of Synapse now shows `--userns keep-id` and no `--pod`. 1.5 also prefers the process environment over `--env-file`, so the Postgres 18 upgrade script exports the image after sourcing `.env`; Valkey keeps `CAP_KILL` so tini can still forward stop signals after `cap_drop ALL`; and the CI check stops and starts Valkey instead of using `podman restart`, which leaves the container exited on the current runner. Coverage held at 95.75 % with `shellcheck`, `ruff` and the bats suite passing.
