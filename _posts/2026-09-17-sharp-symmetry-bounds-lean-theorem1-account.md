---
title: "sharp-symmetry-bounds-lean gains a reviewer's account of Theorem 1"
date: 2026-09-17
tags: [lean4, math, project]
---

[sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean) now
carries a document written for someone checking the formalization rather than reading
it: `docs/THEOREM1.md` gives the informal statement of Theorem 1, a proof outline
mapped step by step to the Lean declarations that carry it, fidelity notes on where the
informal and formal statements diverge, and reproduction instructions
([85ddda8](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/85ddda8)). The
addition makes the informal argument the declared source, since `formalization.yaml` now
points its original-proof source at this document and records the passing mechanical
preflight. A stale comment about sharpness in `lean/DirectBound.lean` was corrected in
the same commit.
