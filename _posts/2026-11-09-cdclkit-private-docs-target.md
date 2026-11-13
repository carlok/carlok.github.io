---
title: "cdclkit: the private-docs target now builds whatever documents docs/private holds"
date: 2026-11-09
tags: [tool]
---

The `private-docs` target in [cdclkit](https://github.com/carlok/cdclkit)'s Makefile listed the untracked documents in `docs/private` by name, so a tracked build file kept a list of files nobody commits. It now builds every `.tex` file the directory holds, which is the only thing that target needs to know ([38867e9](https://github.com/carlok/cdclkit/commit/38867e95003133fcc3428b65caa15efb52621650), [#14](https://github.com/carlok/cdclkit/pull/14)). Nothing else changes, the target still requires the untracked directory to exist, and `make test` passes.
