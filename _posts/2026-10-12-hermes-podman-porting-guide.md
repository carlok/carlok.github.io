---
title: "hermes-podman: the porting guide for a host that already ran Hermes natively"
date: 2026-10-12
tags: [podman, project]
---

[hermes-podman](https://github.com/carlok/hermes-podman) now carries the path it
was missing: the rest of the repository assumes a fresh VM, and
[docs/PORTING-native-install.md](https://github.com/carlok/hermes-podman/blob/main/docs/PORTING-native-install.md)
covers the other arrival — a host that already ran Hermes as a git install, with
`~/.hermes` and a systemd unit, moving into the pinned container
([#2](https://github.com/carlok/hermes-podman/pull/2),
[6e4bba1](https://github.com/carlok/hermes-podman/commit/6e4bba1)). Everything
in it comes from a port actually done against this deployment rather than from
reading the code: what travels (the secrets, `state.db` moved with SQLite's
backup API, and repositories as a bind mount at the same path so absolute cron
workdirs keep resolving, where about 5 of the 2.7 GB home is host-only and must
not be copied), the HOME layout traps — the gateway runs with `HOME=/opt/data`
while interactive sessions get `/opt/data/home`, both real, so scripts and
prompts silently read the wrong `~/.hermes` or `~/projects` until two symlink
shims fix it without editing them — and the tooling the image lacks (`gh`, `jq`,
`tirith`, `himalaya`, `sqlite3`) with a `/opt/data/.local/bin` drop-in that keeps
gh- and jq-based jobs working without touching the image.

The one-off container hazard is the part worth reading twice: s6 brings up a
gateway slot and Hermes loads the real `.env`, so a careless rehearsal can take
the live poller. The guide covers one-poller handover, cutover order, what to
verify from inside, and staged cleanup that keeps the old install as the rollback
path, with `compose.yaml` untouched since machine-local mounts stay in the
gitignored override. It is the repository's second pull request, after
[going public](/blog/2026/10/11/hermes-podman-public/).
