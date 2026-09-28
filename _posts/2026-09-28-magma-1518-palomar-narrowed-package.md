---
title: "magma-1518-obstruction-lean narrows its Palomar package to Theorem A after the registry's automated review"
date: 2026-09-28
tags: [lean4, math, research]
---

Palomar's automated review declined registration of
[magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean)
on two grounds, and both are now answered. The first was an overstatement: the
abstract, the source record and the `Challenge` account presented "no finiteness"
and "one target law instead of four" as a strengthening of the cited conjecture,
while the repository's own prior-work account says the conjecture carried no
finiteness hypothesis — the README and notes had been corrected on 13 September,
the metadata and the `Challenge` docstring were missed, so the repository
contradicted itself in the two places a reviewer reads first
([5d521ea](https://github.com/carlok/magma-1518-obstruction-lean/commit/5d521ea)).
The second was scope: the compared declarations included the F5 and F13 members
of Theorem F, two concrete finite examples rather than the family, and the review
did not find research interest established for that group. The package now
compares **Theorem A and Corollary A′ alone**, `Challenge.lean` falls from 178 to
84 lines, the family facts stay audited under their library names, and
`gen_palomar.py` grew a `--with-family` flag that reproduces the earlier
ten-declaration package
([af908bb](https://github.com/carlok/magma-1518-obstruction-lean/commit/af908bb)).

The pin then moved to **Lean v4.35.0-rc3**, the newest release that clears
Palomar's declared minimum of v4.35.0-rc2 while still letting the verifier derive
its `lean4export` from the Lean version, checked with `lake build`, the axiom
audit and the Comparator
([047895a](https://github.com/carlok/magma-1518-obstruction-lean/commit/047895a)).
Palomar requires its own complete reusable workflow at `mode: full` before a
submission and does not accept a local build or a standalone Comparator run as
equivalent, so a preflight workflow now calls it pinned to the same
`pipeline_commit` ([e61f71f](https://github.com/carlok/magma-1518-obstruction-lean/commit/e61f71f))
— where the second attempt at a clean submission stopped: called from this
repository, that reusable workflow **skips every verification step** and reports
only that the mechanical report was malformed, so the Comparator run was recorded
separately from the pin ([ea94db5](https://github.com/carlok/magma-1518-obstruction-lean/commit/ea94db5))
and the failure was filed upstream as
[PalomarRegistry/PalomarSubmission#154](https://github.com/PalomarRegistry/PalomarSubmission/issues/154).
