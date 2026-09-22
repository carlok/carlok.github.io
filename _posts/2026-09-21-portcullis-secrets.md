---
title: "portcullis stops printing its own secrets and pins the host key across phases"
date: 2026-09-21
tags: [security, tool]
---

[portcullis](https://github.com/carlok/portcullis) hardened its own handling of
the secrets it moves around during provisioning
([f41693f](https://github.com/carlok/portcullis/commit/f41693f)): it no longer
logs the first and last four characters of `HCLOUD_TOKEN`, `keys/id_rsa` is
created `0600` from the start rather than being written and then narrowed, and
the `smtp.env` values are shell-quoted before Phase 2 sources them as root —
passwords containing `$`, spaces, quotes or backticks had been mangled or
executed, and the file is now `chmod 0600` on the VM before credentials are
written into it. Phase 1's SSH host key is pinned and Phase 2 rejects a different
one immediately, so a swapped host cannot receive the second phase's credentials,
and preflight validation now runs before any Hetzner resource exists.
