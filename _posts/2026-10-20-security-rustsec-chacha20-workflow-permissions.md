---
title: "forgepulse, neon-bumper-cars and cross-tetris: RUSTSEC advisories, a yanked chacha20, and a GITHUB_TOKEN that was too wide"
date: 2026-10-20
tags: [security, tool]
---

Three repositories closed their open security alerts in one pass. [forgepulse](https://github.com/carlok/forgepulse) pins `source-map-js` to 1.2.2 through a pnpm override for [GHSA-68fv-2mgg-jv7q](https://github.com/advisories/GHSA-68fv-2mgg-jv7q) — the same parser denial of service [the games took on 17 October](/blog/2026/10/17/dependency-security-proxy-addr/) — moves `quinn`/`quinn-proto` for RUSTSEC-2026-0338, -0340 and -0343, takes `chacha20` 0.10.2 because 0.10.1 was yanked, and enables `sqlx`'s features explicitly with `default-features` off so the dependency set is the one declared ([57f0c29](https://github.com/carlok/forgepulse/commit/57f0c29), [#4](https://github.com/carlok/forgepulse/pull/4)).

[neon-bumper-cars](https://github.com/carlok/neon-bumper-cars) had already shipped the production fix; what was left was the development tree, where `jest` goes to 30.5.2 and drops the vulnerable `micromatch`/`braces` chain, `nodemon` goes to 3.1.14, and npm overrides hold `chokidar` at 4.x and `js-yaml` at 4.x so neither tool pulls the old transitives back in — with the Jest CLI flags updated for v30's `testPathPatterns` ([b7149a9](https://github.com/carlok/neon-bumper-cars/commit/b7149a9), [#9](https://github.com/carlok/neon-bumper-cars/pull/9)). Its production audit was already clean once `proxy-addr` 2.0.8 landed.

[cross-tetris](https://github.com/carlok/cross-tetris)'s alert was CodeQL's `actions/missing-workflow-permissions`: the CI workflow left `GITHUB_TOKEN` at its repository default, so it now declares `permissions: contents: read` at the top of `ci.yml`, the same minimal block the deploy workflow already used ([73d907d](https://github.com/carlok/cross-tetris/commit/73d907d), [#2](https://github.com/carlok/cross-tetris/pull/2)).
