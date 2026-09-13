---
title: "diaz-modulus-lean mirrors the Prove2Me Diaz nodes, and archives all 167 accepted proofs"
date: 2026-09-13
tags: [lean4, math, research]
---

[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) absorbed the
Prove2Me work rather than citing it: `diaz_of_sfe` — strong four exponentials
implies the conjecture — was ported first
([fcf8130](https://github.com/carlok/diaz-modulus-lean/commit/fcf8130)), then
the rest: Hermite–Lindemann is now *proved* here instead of assumed, so
`#print axioms Diaz.diaz_of_sfe` returns only `propext`, `Classical.choice` and
`Quot.sound`, alongside the fibre bound, the quantisation batch, the six
exponentials node and the candidate statements mirrored with their platform
submission ids
([0144e57](https://github.com/carlok/diaz-modulus-lean/commit/0144e57),
[fcf8130](https://github.com/carlok/diaz-modulus-lean/commit/fcf8130),
[e4880ab](https://github.com/carlok/diaz-modulus-lean/commit/e4880ab),
[8d02fd4](https://github.com/carlok/diaz-modulus-lean/commit/8d02fd4),
[7cb8b3a](https://github.com/carlok/diaz-modulus-lean/commit/7cb8b3a)). The
repository also gained a complete copy of the mission:
[archive/prove2me/](https://github.com/carlok/diaz-modulus-lean/tree/main/archive/prove2me)
holds all 167 accepted submissions for its 132 Proved nodes plus a manifest, so
no proof of this mission exists only on the platform
([1f05ae7](https://github.com/carlok/diaz-modulus-lean/commit/1f05ae7)) — kept
deliberately unbuilt, since the files target the platform's Mathlib revision and
nothing in CI reads them, with
[scripts/refresh_prove2me_archive.py](https://github.com/carlok/diaz-modulus-lean/blob/main/scripts/refresh_prove2me_archive.py)
refreshing the archive and `--check` failing when it goes stale
([735f5b4](https://github.com/carlok/diaz-modulus-lean/commit/735f5b4)). The
companion note is published as
[tex/diaz_prove2me.tex](https://github.com/carlok/diaz-modulus-lean/blob/main/tex/diaz_prove2me.tex)
and the CI build was fixed by dropping a `says-verified` simp list
([e8265ae](https://github.com/carlok/diaz-modulus-lean/commit/e8265ae)).
