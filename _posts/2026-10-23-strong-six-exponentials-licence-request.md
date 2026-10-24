---
title: "contributed to telaviv/strong-six-exponentials: a licence request, so a theorem becomes a dependency"
date: 2026-10-23
tags: [contribution, lean4, math]
---

[strong-six-exponentials](https://github.com/telaviv/strong-six-exponentials) is someone else's Lean 4 formalisation of Roy's strong six exponentials theorem — public since 18 October, on the same Lean and Mathlib revision — and it is the one hypothesis standing between [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) and a batch of unconditional results: the library's theorems take that theorem as the hypothesis `hSSE`, and the two statements are a short bridge apart. So the contribution to that project is a question rather than a patch, [issue #1](https://github.com/telaviv/strong-six-exponentials/issues/1) opened on 23 October and addressed to Shawn Krisman: the repository has no `LICENSE` file while its file headers say Apache 2.0, so a licence with a named copyright holder is what would let the work depend on it through Lake, with credit in the README and the companion note.

The second question is about the port. Those results also live on the Prove2Me platform under Apache 2.0, so the issue asks whether a port of the proof is welcome there credited to its author — or whether he would rather submit it himself, or not have it there at all. All three answers are explicitly fine; the issue is open with no reply yet.
