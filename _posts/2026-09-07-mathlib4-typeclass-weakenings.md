---
title: "contributed to mathlib4: #43503 bundles 32 mechanically found typeclass weakenings"
date: 2026-09-07
tags: [lean4, math, contribution]
---

Contributed to
[leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4):
[PR #43503](https://github.com/leanprover-community/mathlib4/pull/43503)
weakens unused typeclass assumptions on section variables across 29 files —
32 one-line changes, 32 insertions and 32 deletions. Each was found by the
[unused-assumptions](https://github.com/carlok/unused-assumptions) pipeline
(LLM + Lean 4 propose, the compiler decides): replace one binder with a weaker
class, keep the proof unchanged, compile it alone. Every change built against
its unmodified file, with the whole library compiling locally at `633b366493`.
It is one PR rather than many by deliberate choice, citing mathlib's own
[#42214](https://github.com/leanprover-community/mathlib4/pull/42214) (813
files of the same kind of change) as precedent; the background is on the
[mathlib Zulip](https://leanprover.zulipchat.com/#narrow/channel/287929-mathlib4/topic/unused.20hypotheses.3A.20431.20in.20a.2029k.20sample.2C.20and.2033.20one-line.20PRs/near/622113682),
where a reader spotted a further simplification in one refactored file.
