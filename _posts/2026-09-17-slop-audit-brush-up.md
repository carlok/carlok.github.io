---
title: "slop-audit: the brush-up pass, and the rename to slop_audit"
date: 2026-09-17
tags: [tool]
---

[slop-audit](https://github.com/carlok/slop-audit) spent the rest of the week
being made presentable rather than more capable. A
[brush-up design](https://github.com/carlok/slop-audit/commit/4906f8e) split
the work into Phase 1 (docs and packaging) and Phase 2 (hygiene), and Phase 1
followed: an MIT license, a changelog and `pyproject.toml` metadata
([e7bc0a3](https://github.com/carlok/slop-audit/commit/e7bc0a3)) with the
README polished and GitHub publication marked done
([9b6a418](https://github.com/carlok/slop-audit/commit/9b6a418)), merged as
[PR #1](https://github.com/carlok/slop-audit/pull/1).

Phase 2 then renamed the import package `text_audit` → `slop_audit` so it
matches the distribution name, and wired the live independent-agreement /
corroborated findings into the report — restricted to the style, slop and prose
tools, which is the side of the harness that has something to corroborate
([07ccaaf](https://github.com/carlok/slop-audit/commit/07ccaaf),
[PR #2](https://github.com/carlok/slop-audit/pull/2)). The changelog notes the
package was `text_audit` until Phase 2, because the rename is the one change
the 0.1.0 entry could not describe.
