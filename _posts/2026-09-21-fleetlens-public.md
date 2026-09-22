---
title: "fleetlens is public: agentless health reports for a small VM fleet"
date: 2026-09-21
tags: [tool, project]
---

[fleetlens](https://github.com/carlok/fleetlens) is now public: for a handful of
Debian/Ubuntu VMs it logs in over SSH with Ansible, collects a fixed set of
read-only facts and turns them into a JSON report, a Markdown report, a terminal
summary and an optional email — nothing installed on the targets and nothing on
them changed. It sits between "I SSH in and look around every few weeks" and a
full monitoring stack: disk usage, pending updates, reboot-required, failed
units and journal errors, with each host marked OK, WARNING or CRITICAL and the
fleet taking the worst of them.

The [0.2.0 release](https://github.com/carlok/fleetlens/releases/tag/v0.2.0),
cut as the repository was opened, is mostly a list of silent failures fixed
first: disk WARNING and CRITICAL results never reached the report because the
collector emitted statuses with trailing whitespace the classifier did not match,
hosts whose collection aborted were dropped from the report entirely instead of
appearing as CRITICAL, and a single unreachable host made the playbook exit
non-zero and abort the run before anything was rendered — so a failed check could
look like no check at all
([45e0b73](https://github.com/carlok/fleetlens/commit/45e0b73),
[dacc5d1](https://github.com/carlok/fleetlens/commit/dacc5d1)). The release adds
`--fail-on none|warning|critical` for scheduler-visible exit codes, `email --force`,
and a `fleetlens` console script; the container-era build prompt is gone.
