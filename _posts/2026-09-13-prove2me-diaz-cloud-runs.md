---
title: "prove2me-logs: two cloud runs on the Diaz mission, and a helper that stops mangling LaTeX"
date: 2026-09-13
tags: [lean4, math, prove2me]
---

[prove2me-logs](https://github.com/carlok/prove2me-logs) records the Diaz
mission being worked by a cloud agent with nothing but a Prove2Me key, a GitHub
token and the public brief: the
[first run](https://github.com/carlok/prove2me-logs/commit/028fe0d) proved
`DiazModulus.candidate_no_real_algebraic_line`, the
[second](https://github.com/carlok/prove2me-logs/commit/40ef630) added
`candidate_distance_transcendental` by polarization on top of the first run's
line exclusion — both accepted, both mirrored into
[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean). Offline the
same day, the
[multiplier module](https://github.com/carlok/prove2me-logs/commit/f7e8cff)
determined what an extension of the three-dimensional hull could be
(`{z : u·z ∈ L̃} = Q̄ + Q̄/u`, so no shifted reciprocal survives) and the one-log
saturation node ruled out a candidate inside `Q̄ + Q̄·l`. The session's most
useful artifact is a
[curl-free helper](https://github.com/carlok/prove2me-logs/commit/147e2c5):
passing a JSON body through a double-quoted shell string let bash expand `$u`,
`$v` and `$$` inside the LaTeX before the request went out, which wrote mangled
mathematics into 52 published nodes — repaired from a pre-damage snapshot — and
`tools/p2m.py` now builds the multipart request itself and accepts any body as
`@file`.
