---
title: "pickmydegree: npm overrides clear four moderate audit findings in the Surge build toolchain"
date: 2026-11-04
tags: [project, security]
---

[pickmydegree](https://github.com/carlok/pickmydegree) raised its npm overrides for the Surge dev tooling that publishes the built site — `glob` to `^14.0.4` and `minimatch` to `^11.0.5`, with `rimraf` deliberately left at `^5.0.5` — which clears four moderate `npm audit` findings against the previous lockfile while leaving every application runtime dependency where it was ([937f589](https://github.com/carlok/pickmydegree/commit/937f589), [#15](https://github.com/carlok/pickmydegree/pull/15)). The same week's two other dependency pull requests stay inside the i18n stack: `vue-i18n` with `@intlify/core-base` ([#12](https://github.com/carlok/pickmydegree/pull/12)) and `vue-i18n` with `@intlify/shared` ([#13](https://github.com/carlok/pickmydegree/pull/13)). The overrides rather than a plain bump matter because the advisories sit under `glob` and `minimatch` reached through the deploy tool, not under anything the app itself imports.
