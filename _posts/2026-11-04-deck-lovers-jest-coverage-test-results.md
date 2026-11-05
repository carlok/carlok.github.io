---
title: "deck-lovers: Jest coverage writes to test-results/, so the Actions runner stops hitting EACCES"
date: 2026-11-04
tags: [tool]
---

Jest in [deck-lovers](https://github.com/carlok/deck-lovers) was told to write HTML coverage to an absolute `/reports/converter-js` and `/reports/server-js`, a path that exists inside the project's own test image but not on a GitHub Actions runner, where `npm test -- --ci` then fails writing the report. Both `coverageDirectory` values now point at `../test-results/*` relative to each workspace ([0a532fa](https://github.com/carlok/deck-lovers/commit/0a532fa)), while the Podman test image keeps passing its own `--coverageDirectory` overrides from `Dockerfile.js.test`, so the container path is unchanged. The change sits on `daily-care/2026-11-04-jest-coverage-path` as [#7](https://github.com/carlok/deck-lovers/pull/7), open at the time of writing.
