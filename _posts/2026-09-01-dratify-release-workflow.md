---
title: "dratify: the release workflow now tests the tag it publishes"
date: 2026-09-01
tags: [rust, tool]
---

[dratify](https://github.com/carlok/dratify)'s release pipeline could report a
successful release that published nothing: `ci.yml` triggers on branches and
pull requests and never on tags, so no test ever ran against the ref being
published, and combined with `skip-existing` a tag that forgot to bump the
version built the old one, had PyPI skip it as already present, and exited
green. The suite now
[runs on the tag, and the build fails when the tag does not name the version it
produced](https://github.com/carlok/dratify/commit/9b414fc) — `skip-existing`
should absorb a re-run of the same release, not disguise a forgotten bump.
