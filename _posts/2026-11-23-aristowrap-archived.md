---
title: "aristowrap is archived: the Docker wrapper around Harmonic's Aristotle goes read-only at v0.1.1"
date: 2026-11-23
tags: [project, tool]
---

[aristowrap](https://github.com/carlok/aristowrap) was archived on 23 November: the repository is read-only, no further updates, fixes or releases are planned, issues and pull requests are no longer monitored, and the published images and tags are left as they are ([86ddea1](https://github.com/carlok/aristowrap/commit/86ddea1)). The last release is [v0.1.1](https://github.com/carlok/aristowrap/releases/tag/v0.1.1).

The README now opens by saying so, and keeps what the tool was for: a small CLI that runs Lean 4 and Harmonic's `aristotle` inside Docker or Podman so that elan, Lake and Python stay off the host — `submit` staging a copy of a Lake and Lean tree to the service and waiting by default for a `solution-*.tar.gz`, `verify` unpacking one and running `lake build` — with the caveat it always carried, that it is unofficial and not affiliated with Harmonic. The note ends with the only instruction left, to fork it if you want to carry it on.
