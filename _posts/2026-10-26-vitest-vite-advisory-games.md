---
title: "storygen, eclipse-3d-sim, collective-starship-game, agility-trainer and solids-hunter: one vitest advisory, five repositories"
date: 2026-10-26
tags: [security, games]
---

The same test-runner advisory reached five of the game repositories, and each took `vitest` 4.1.12 for it: GHSA-xp26-3454-mjgp, a Windows backslash traversal that bypasses `@vitest/mocker`'s redirect allow-list. [storygen](https://github.com/carlok/storygen) bumped vitest ([#7](https://github.com/carlok/storygen/pull/7), [6a9e3a5](https://github.com/carlok/storygen/commit/6a9e3a5)) and then `vite` to 6.4.5 ([#9](https://github.com/carlok/storygen/pull/9), [a2ad1a5](https://github.com/carlok/storygen/commit/a2ad1a5)); [eclipse-3d-sim](https://github.com/carlok/eclipse-3d-sim) did both ([#3](https://github.com/carlok/eclipse-3d-sim/pull/3), [#4](https://github.com/carlok/eclipse-3d-sim/pull/4)); [collective-starship-game](https://github.com/carlok/collective-starship-game) took vitest 4.1.12 together with the transitive packages behind it ([#7](https://github.com/carlok/collective-starship-game/pull/7), [e7c157c](https://github.com/carlok/collective-starship-game/commit/e7c157c)).

[agility-trainer](https://github.com/carlok/agility-trainer) ([#3](https://github.com/carlok/agility-trainer/pull/3)) and [solids-hunter](https://github.com/carlok/solids-hunter) ([#2](https://github.com/carlok/solids-hunter/pull/2), [3ceb272](https://github.com/carlok/solids-hunter/commit/3ceb272)) took vitest and vite 6.4.5 together. Vitest is a test-time dependency, so no game logic changed; the vite move is the 6.4.4+ line, where the dev-server advisories are fixed.
