---
title: "A dependency-advisory sweep across the JavaScript, Python and Go repositories"
date: 2026-09-21
tags: [security, github]
---

A pass over open dependency advisories bumped the affected packages in every
repository that carried them. On the JavaScript side:
[pickmydegree](https://github.com/carlok/pickmydegree/commit/63ae859) (`vitest`,
`happy-dom`, `vite`, `surge`),
[storygen](https://github.com/carlok/storygen/commit/e690385) (`vitest` 4, `vite`
6, `react-router` 7), [solids-hunter](https://github.com/carlok/solids-hunter/commit/ea1885e)
(`vitest` 4, `vite` 6.4.3), [eclipse-3d-sim](https://github.com/carlok/eclipse-3d-sim/commit/796120e),
[lifechess](https://github.com/carlok/lifechess/commit/bea3955),
[agility-trainer](https://github.com/carlok/agility-trainer/commit/787e5cf) and
[they-live-agent](https://github.com/carlok/they-live-agent/commit/b90eff0)
(`vitest` 4.1.11), [platosdf](https://github.com/carlok/platosdf/commit/d55ca87)
(`vitest` and its coverage package, 5.0.1), with lockfile refreshes in
[deck-lovers](https://github.com/carlok/deck-lovers/commit/0652c20) and `express`
updates in [neon-bumper-cars](https://github.com/carlok/neon-bumper-cars/commit/b89493a)
and [collective-starship-game](https://github.com/carlok/collective-starship-game/commit/dbc0c64).

On the Python and Go side:
[portcullis](https://github.com/carlok/portcullis/commit/7e4527a) (`cryptography`,
`paramiko`, `pytest`), [caciarabot](https://github.com/carlok/caciarabot/commit/1fdd5bc)
(`pytest` 9.x, for the `tmpdir` advisory),
[pacenotch](https://github.com/carlok/pacenotch/commit/9b7f8a6) (`golang.org/x/image`,
`golang.org/x/net`), [forgepulse](https://github.com/carlok/forgepulse/commit/2a19feb)
(`vitest` 4.1.11 and `echarts` 6.1.0), and a routine `pytest` bump in
[aristowrap](https://github.com/carlok/aristowrap/commit/90ca880). One removal rode
along: [collective-starship-game](https://github.com/carlok/collective-starship-game/commit/7206463)
dropped the leftover AI Studio wiring — a `GEMINI_API_KEY` define and a
`.env.example` nothing read — and uninstalled five dependencies that no module
imports.
