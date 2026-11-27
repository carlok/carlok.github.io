---
title: "cdclkit 0.2.2: two flags the command line accepted and then ignored, and a release that cannot publish half of itself"
date: 2026-11-26
tags: [tool]
---

The `maintenance-2026-11` branch of [cdclkit](https://github.com/carlok/cdclkit) carries 0.2.2, and both of its fixes are flags the command line accepted and then dropped. `-j N` ran the extra workers on their own settings, so `cdclkit solve -j 2 --restart none` used neither, and `--var-decay`, `--ccmin`, `--no-phase-saving`, `--rnd-freq` and `--seed` went the same way; `--adaptive` always ran three preprocessing rounds because `--prep-rounds` was never passed on, so the library's `solve_adaptive` now takes `prep_rounds` and a negative count raises `ValueError` where the native engine used to raise `OverflowError` and Python silently ran no rounds ([CHANGELOG](https://github.com/carlok/cdclkit/blob/maintenance-2026-11/CHANGELOG.md)).

The release machinery changed with them. Neither PyPI job starts until every build has passed, after 0.2.0 reached PyPI while its native wheels were still failing, and every tag now gets a GitHub Release whose notes are that tag's CHANGELOG section, with the build failing if the section is missing — until now no tag had one, and the manual `gh release create` that `docs/RELEASING.md` asked for was simply never run ([4fc29d3](https://github.com/carlok/cdclkit/commit/4fc29d3)).

Two smaller repairs came along: `make smoke` could never resolve cdclkit's one dependency, installing it `--no-index` from a `dist/` that holds no dratify, and now installs dratify from PyPI first while the offline step still takes both wheels from `dist/` and writes its CNF into `.smoke/`; and `make dist` looks for the build package outside the checkout instead of assuming it sits in the tree ([31aa46e](https://github.com/carlok/cdclkit/commit/31aa46e), [18c84fb](https://github.com/carlok/cdclkit/commit/18c84fb)). The native manifest now says Rust 1.85, which is what the locked pyo3 already required while the file claimed 1.70, and CI builds with exactly that ([7c01024](https://github.com/carlok/cdclkit/commit/7c01024)).
