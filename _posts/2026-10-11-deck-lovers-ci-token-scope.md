---
title: "deck-lovers: the CI token is scoped to read-only contents"
date: 2026-10-11
tags: [tool, security]
---

[deck-lovers](https://github.com/carlok/deck-lovers)' CI workflow declared no
`permissions` block, so every run inherited the repository's default token
scope — read/write on the repository's contents, for a job that only checks out
the code and runs the tests. It now asks for `contents: read`
([9c30dae](https://github.com/carlok/deck-lovers/commit/9c30dae)), the same
scoping [forgepulse](/blog/2026/09/28/forgepulse-star-feed/) got after a CodeQL
alert on its workflow.
