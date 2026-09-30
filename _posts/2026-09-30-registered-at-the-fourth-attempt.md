---
title: "Registered at the fourth attempt"
date: 2026-09-30
tags: [lean4, math, research]
---

On 29 November 2024 Terence Tao conjectured on the Lean Zulip that the only
nontrivial one-generated magma satisfying law 1518 of the Equational Theories
Project, together with four target laws, is the three-element cyclic shift. I
proved it in core Lean this month, in
[magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean).
Since 30 September it is a registry record:
[PALOMAR-2026-09-30-000005](https://palomar-registry.org/entry?id=PALOMAR-2026-09-30-000005&version=1).

Palomar does not take my word for it. It rebuilt the project in a sandbox,
exported the proof terms, replayed them with two independent kernels, and ran
the Comparator to check that the solution proves exactly the stated theorems
using only the three standard axioms. The record certifies that the proofs
check. It says nothing about novelty, and neither do I: the searchable venues
were checked and nothing was found, which is not a proof that nothing exists.

It took four submissions.

**The first was verified in three minutes and then stopped at review.** The
automated editorial review found two problems. My abstract presented "no
finiteness hypothesis" and "one target law instead of four" as strengthening
Tao's conjecture. But Tao's message carried no finiteness hypothesis, and
Matthew Bolan had noted the same day that the one law already implies the other
three. My own repository said so, in another file, and the reviewer read both.
The second problem was that I had also submitted two concrete finite models,
the 15- and 39-element members of a family, and on their own they did not make
a case for research interest. Fair on both counts. I corrected the claim
everywhere it appeared and
[narrowed the package](/blog/2026/09/28/magma-1518-palomar-narrowed-package/)
to the four declarations of the classification.

**The second passed on the mathematics and failed on the README**, which still
described the earlier ten-declaration package. The configuration checked four;
the front page implied ten.

**The third never reached verification.** Palomar had just added a preliminary
rule: every `.lean` file in the repository must begin with the `module` header.
[Porting sixteen files](/blog/2026/09/28/magma-1518-module-system-port/) was
mechanical except for one trap. The `bv_decide` census
files need an extra meta import, and without it every `bv_decide` call fails and
the census theorems end up resting on `sorryAx`.

**The fourth was verified and reviewed without warnings**, and I asked for
registration on 28 September at 08:09 UTC. Then nothing happened for 41 hours.
The registry had all but
[stopped creating archive copies](/blog/2026/09/28/palomar-registration-stalled/),
for everyone; one
submission stuck in a retry loop appears to have been holding the queue. It
started moving again overnight, without an announcement, and the record was
issued at 01:30 UTC.

The record is narrower than the repository. It covers Theorem A only. The
cohomological obstruction and the explicit family of countermodels stay in the
repository, some of it kernel-checked and some of it computation or written
proof, none of it inside the record.

The Lean was right from the first submission. What failed twice was the text
around it: a claim stronger than the one I had already made elsewhere, and a
README describing a package I was no longer submitting. It took an automated
reviewer to hold the prose to the standard the kernel holds the proofs to.
