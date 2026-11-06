---
title: "dratify and cdclkit: CI now runs the gate CONTRIBUTING promised, on the Python floor and against two other solvers"
date: 2026-11-05
tags: [tool]
---

[cdclkit](https://github.com/carlok/cdclkit) had been skipping two steps its `CONTRIBUTING.md` said ran as part of `make gate` — `make lint` and `bench/compare.py --quick` — and CI now runs both, with a new `agreement` job comparing the solver's answers against MiniSat and CaDiCaL ([#13](https://github.com/carlok/cdclkit/pull/13), [f54f106](https://github.com/carlok/cdclkit/commit/f54f106)). The same pass adds `.github/workflows/audit.yml` for `cargo audit` over `native/Cargo.lock`, on every lockfile change and weekly, and a Dependabot pip entry for the build tooling, with `dratify` and `cdclkit-native` excluded because their versions move only with a release.

[dratify](https://github.com/carlok/dratify) closed the complementary hole the same afternoon: its tests only reach what they import, so a syntax error in a script nothing imports could ship unnoticed. A new lint job runs `compileall` over `src`, `tests` and `bench` on Python 3.10 — the oldest supported version — which also catches syntax too new for the `requires-python` floor, and `make lint` runs the same check before `cargo test` and `clippy` so a local run and the runner agree ([#14](https://github.com/carlok/dratify/pull/14), [db52e80](https://github.com/carlok/dratify/commit/db52e80)).
