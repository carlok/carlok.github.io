---
title: "unused-assumptions: the published repository learns what to keep out"
date: 2026-09-10
tags: [lean4, math, research]
---

The [unused-assumptions](https://github.com/carlok/unused-assumptions) repository
now separates what is published from what is merely being worked on: `outreach/`
workshop text for upstream pull requests and messages — including other people's
contact details and prose that is not its author's to publish — is ignored at the
root rather than parked in a sibling repository
([43e092a](https://github.com/carlok/unused-assumptions/commit/43e092a)), since the
drafts are about this project's results and belong beside them. The same instinct
ran through the leak-detector test, which had been asserting that no shipped tool
names the private sibling project while spelling out exactly those names as
literals — now assembled from fragments so the repository stops carrying the one
string it exists to withhold
([3e1cb9a](https://github.com/carlok/unused-assumptions/commit/3e1cb9a),
[78ce2c0](https://github.com/carlok/unused-assumptions/commit/78ce2c0)). One
weakening was also withdrawn as unwanted despite compiling
([b0e1f4f](https://github.com/carlok/unused-assumptions/commit/b0e1f4f)): a patch
surviving the compiler is not the same as a patch worth publishing.
