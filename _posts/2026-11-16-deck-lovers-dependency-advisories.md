---
title: "deck-lovers: two critical advisories in the Python stack, and deepmerge pinned to a commit npm never released"
date: 2026-11-16
tags: [security, tool]
---

[deck-lovers](https://github.com/carlok/deck-lovers) closed every dependency advisory `osv-scanner` could see in one pass ([#30](https://github.com/carlok/deck-lovers/pull/30), [f79e538](https://github.com/carlok/deck-lovers/commit/f79e538)), after the Dependabot alerts API answered 403 for the integration token. Two were Critical at an OSV CVSS of 9.1 — `h11` moved to `>=0.16.0` and `certifi` to `>=2026.10.18` on the server requirements — with `idna` to `>=3.15`, and the npm dev side took `glob >=14.0.2`, `minimatch >=11.0.1` and `deepmerge`, whose advisory has no patched npm release at all, so the override points at the fix commit `c5ad573` from TehShrike/deepmerge#273 rather than at a version.

The verification is in the PR: `osv-scanner -r .` reports no issues, the converter's Python tests are 126 passed at 91.73% coverage against a floor of 88 and the server's 59 passed at 93.33% against 89, Jest runs 29 and 26 tests at 100% on `*.pure.js`, and `./tests/deploy_test.sh` passes 35. `npm audit` will keep listing `deepmerge@4.3.1` until that release exists, which is why the override is documented as something to drop rather than a fix that stays.
