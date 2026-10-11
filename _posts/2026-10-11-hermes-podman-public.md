---
title: "hermes-podman is public: the headless Hermes Agent gateway on rootless Podman"
date: 2026-10-11
tags: [podman, project]
---

[hermes-podman](https://github.com/carlok/hermes-podman) is now public: the
deployment behind this site's own agent gateway, written down as a repository
instead of shell history. A Hermes Agent container
([`nousresearch/hermes-agent:v0.21.6`](https://github.com/carlok/hermes-podman/blob/main/compose.yaml),
pinned by digest as well as tag) runs rootless under Podman and podman-compose
on an Ubuntu 26.04 host — as the normal user, with `userns keep-id` so `data/`
stays owned by that user, in `gateway run` mode only: no dashboard, no published
ports, no browser tools, everything mutable in one `BASE_DIR/data` mounted at
`/opt/data` ([698f8af](https://github.com/carlok/hermes-podman/commit/698f8af)).
A Makefile and scripts cover setup, up/down, verify, logs, chat, backup,
restore, upgrade and uninstall, a Quadlet unit is offered as the compose
alternative, CI exercises the whole lifecycle, and
[docs/DECISIONS.md](https://github.com/carlok/hermes-podman/blob/main/docs/DECISIONS.md)
records why each of those choices was made.

The first day's work was about what a real host knows and CI cannot. A power
cycle exposed that the vendor `podman-restart.service` is `Type=oneshot` and
loses the boot race on Ubuntu 26.04 — AppArmor profiles load progressively there
and the re-exec fails with `Permission denied` — so the deployment stayed down
until someone ran `make up`; `deploy/podman-restart-retry.conf` replaces only
`ExecStart` with a bounded 30×4 s retry and no sysctl or AppArmor change, and
the next real reboot brought the same container back about 20 s in, while
`verify.sh` stopped accepting a banner from the previous start and gives the s6
slot up to 60 s ([7af370c](https://github.com/carlok/hermes-podman/commit/7af370c),
[#1](https://github.com/carlok/hermes-podman/pull/1)). `compose.yaml` also went
back to the portable definition: a machine-local mount added for one host makes
podman abort on every host that lacks that path, so extra mounts now live in a
gitignored `compose.override.yaml` that `make` merges when it exists
([fed68c3](https://github.com/carlok/hermes-podman/commit/fed68c3),
[43f72ed](https://github.com/carlok/hermes-podman/commit/43f72ed)). CI moved to
the ubuntu-26.04 probe with the Podman 5 differences documented, a `podman stop`
that exits 125 only because its network cleanup failed is tolerated, and compose
pods are disabled so `keep-id` and `--userns` cannot collide
([85dbd22](https://github.com/carlok/hermes-podman/commit/85dbd22),
[21dfca3](https://github.com/carlok/hermes-podman/commit/21dfca3),
[599dfc1](https://github.com/carlok/hermes-podman/commit/599dfc1),
[b83c964](https://github.com/carlok/hermes-podman/commit/b83c964)).
