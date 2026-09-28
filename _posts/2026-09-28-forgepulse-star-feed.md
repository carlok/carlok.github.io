---
title: "forgepulse: a fleet-wide feed of every star, newest first"
date: 2026-09-28
tags: [rust, tool]
---

[forgepulse](https://github.com/carlok/forgepulse) can now answer "who starred
what, and when" across the whole fleet: a new `/stars` page lists every star
across every tracked repository in one chronological feed — avatar, who, which
repository, when — which GitHub only offers per repository and never across an
account ([af4a8ea](https://github.com/carlok/forgepulse/commit/af4a8ea)). The
backend adds a `star_events` table populated from each repository's
`/stargazers` endpoint requested with the `star+json` media type, which carries
the true `starred_at` per user and so needs no backfill wait, unlike the
human-attention baselines; it syncs alongside the existing star count.

That feed needed an entry point, and the homepage's aggregate Stars figure had
none, so clicking it now switches to clone-volume mode sorted by stars
descending ([e3c89eb](https://github.com/carlok/forgepulse/commit/e3c89eb)),
while each repository's own star count links to its GitHub stargazers page
([68a54c9](https://github.com/carlok/forgepulse/commit/68a54c9)). A CodeQL alert
also closed: the CI workflow had no `permissions` block and therefore ran with
the repository's default token scope, so it is now scoped `contents: read`
([fc7068f](https://github.com/carlok/forgepulse/commit/fc7068f)).
