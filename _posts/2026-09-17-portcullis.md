---
title: "portcullis: a two-phase hardened Ubuntu VM for Hetzner Cloud"
date: 2026-09-17
tags: [security, tool]
---

[portcullis](https://github.com/carlok/portcullis) is a new public Python
repository: one command creates a hardened Ubuntu 26.04 VM on Hetzner Cloud, and
it drops the gate first — an unprivileged user with key-only SSH on a random high
port, root locked, UFW default-deny and sysctl hardening, all inside about 30
seconds and using only what the stock image already ships — then switches the
Hetzner firewall to the new port and deletes the temporary API key before the
full CIS-style pass (package upgrades, AppArmor, auditd, AIDE, PAM policy,
fail2ban, rkhunter, msmtp alerts, Docker and Podman) runs behind both firewalls.
[`verify.sh`](https://github.com/carlok/portcullis/blob/main/verify.sh) then runs
58 checks on the finished host. Everything runs inside a Podman container so
nothing is installed locally, and teardown deletes a half-provisioned server
together with the keys and firewalls it created. The
[README was rebranded](https://github.com/carlok/portcullis/commit/7422f41) as
the repository went public, with a
[GitHub Actions test workflow](https://github.com/carlok/portcullis/commit/07e663c)
on `actions/checkout@v5` and a
[logo](https://github.com/carlok/portcullis/commit/2e89619).
