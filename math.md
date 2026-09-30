---
title: Mathematics
section: math
permalink: /math/
---

<div class="window">
  <div class="titlebar">
    <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
    <span class="filename">carlok — zsh — 88×30</span>
  </div>
  <div class="pane hero-split">
    <img class="avatar" src="https://github.com/carlok.png?size=460" alt="Carlo Perassi">
    <div class="hero-body">
      <p class="prompt">$ <b>cat math/STATUS.md</b></p>
      <h1 class="hero-title">Mathematics<span class="cursor"></span></h1>
      <p class="tagline">
        What is proved, what is still open, and where the evidence lives. The
        <a href="/blog/">blog</a> records the work as it happens and
        <a href="/projects/">projects</a> lists the repositories; this page is the
        standing state of each line, with its limits stated.
      </p>
      {% include social.html %}
    </div>
  </div>
</div>

<div class="tabbar">
  <a class="tab" href="/">home.sh</a>
  <a class="tab" href="/projects/">projects.sh</a>
  <a class="tab" href="/blog/">blog.sh</a>
  <a class="tab" href="/writing/">writing.sh</a>
  <a class="tab active" href="/math/">math.sh</a>
  <a class="tab" href="/cv/">cv.sh</a>
</div>

## Externally registered

Three results carry a record issued by someone other than me. In each case an
independent party re-checked the Lean proofs; no record says the result is new.

- [sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean) — sharp symmetry bounds for real plane algebraic curves, registered as [PALOMAR-2026-09-18-000007](https://palomar-registry.org/entry?id=PALOMAR-2026-09-18-000007&version=1). The registry rebuilt the project in a sandbox, replayed the proof terms with an independent kernel and ran the Comparator. **Limit:** the public extraction covers Theorem 1 only.
- [magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean) — one-generated (1518 + 3862)-magmas are trivial or the Z/3 shift, registered as [PALOMAR-2026-09-30-000005](https://palomar-registry.org/entry?id=PALOMAR-2026-09-30-000005&version=1). The registry rebuilt the project in a sandbox, replayed the proof terms with two independent kernels and ran the Comparator. The conjecture is Terence Tao's (Lean Zulip, 2024-11-29); what this adds is a proof, not a weaker hypothesis. **On priority:** the searchable venues were checked and nothing was found, which is not the same as a proof that nothing exists. **Limit:** the record covers Theorem A only; the cohomology obstruction and the explicit family of countermodels stay in the repository, outside it.
- [moebius-transcendental-lean](https://github.com/carlok/moebius-transcendental-lean) — the conjugation degree on the transcendental locus, archived on Zenodo under concept DOI [10.5281/zenodo.22146649](https://doi.org/10.5281/zenodo.22146649). The small public piece of the Diaz work, and the one that closes a question rather than opening one.

## Proved, with the limit named

- [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) — the large formalization. Since 24 September 2026 Gelfond–Schneider is a tree of eleven modules totalling 1,531 lines, restructuring the single 5,388-line formalization of M. Karatarakis and F. Wiedijk (arXiv:2603.24823, Apache-2.0). Nothing is declared as an axiom any more: the chains rest on Lean's own axioms. **Limit:** Diaz's conjecture itself remains open; the formalization maps the boundary rather than crossing it.
- [erdos-straus-offset-lean](https://github.com/carlok/erdos-straus-offset-lean) — a Lean-verified fixed-divisor offset construction for 4/n = 1/x + 1/y + 1/z. **Limit:** the Erdős–Straus conjecture remains open; this is the construction, not a proof.

## Open, and stated as open

- Diaz's conjecture. The companion note to `diaz-modulus-lean` carries the boundary: each part of the conjecture is closed or reduced to one of three open statements, each named in the note. Two barrier results say which configurations cannot detect a candidate.
- Whether [quadratula](https://github.com/carlok/quadratula) should be certified in Lean. Today it is computational: exhaustive enumeration to order 6, exact results to order 9, and a provably optimal 17-quasigroup cover, with independent checks against the enumerator, OEIS A076017 and Mace4. **Nothing in it is certified in Lean**, and the OEIS matches are leads, not proofs.

## Machine-generated mathematics

- [LeanFrontier](https://carlok.github.io/LeanFrontier/) — an open Lean 4 library of machine-generated, kernel-verified mathematics on Mathlib. Contributions are accepted on their mechanically checked properties: no `sorry`, no custom axioms, no dependency on axioms outside the explicit allowlist.
- [prove2me-logs](https://github.com/carlok/prove2me-logs) — the working log: per-mission entries with theorem uuids, Lean environments, and what remains open below each one. Not a proof archive, and it carries correction notes on entries a later literature reading overturned.
- [lean-corpus-density](https://github.com/carlok/lean-corpus-density) — dependency density in human and machine-generated Lean corpora, reproducible from file headers.

## Tools that came out of the above

- [unused-assumptions](https://github.com/carlok/unused-assumptions) and [unstated-conclusions](https://github.com/carlok/unstated-conclusions) — Mathlib theorems that assume more than their proof needs, and the dual: those whose proofs establish more than they state. Each one re-verified by the compiler at a pinned revision.
- [parsimagma](https://github.com/carlok/parsimagma) — magma signature and coverage over the Equational Theories Project law set.
- [dratify](https://github.com/carlok/dratify) and [cdclkit](https://github.com/carlok/cdclkit) — a DRAT/DRUP proof checker, and a CDCL SAT solver where every answer ships a certificate: models re-checked, UNSAT backed by a proof an independent checker replays.
- [euclean](https://github.com/carlok/euclean) — can a machine recover mathematical structure from an anonymized formal theory and a proof checker alone?

<p class="cmd">cat DISCLAIMER.txt</p>

This page lists only work that is public and checkable today. Work in progress
is not listed here until it is published, and a record of verification is a
statement that the proofs check, not that the result is new.
