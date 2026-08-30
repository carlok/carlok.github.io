---
title: "forgepulse: repos above the fleet's median clone count"
date: 2026-08-30
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse) now highlights repositories
whose clone counts sit above the fleet's median, and the comparison was fixed
to use each repo's own daily median against the fleet's rather than its raw
total, so a busy repo can no longer skew its own marker.
