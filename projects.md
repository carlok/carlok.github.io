---
title: Projects
section: projects
permalink: /projects/
---

<div class="window">
  <div class="titlebar">
    <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
    <span class="filename">carlok — zsh — 88×30</span>
  </div>
  <div class="pane hero-split">
    <img class="avatar" src="https://github.com/carlok.png?size=460" alt="Carlo Perassi">
    <div class="hero-body">
      <p class="prompt">$ <b>cat projects/README.md</b></p>
      <h1 class="hero-title">Projects<span class="cursor"></span></h1>
      <p class="tagline">A curated map of public GitHub work. It favors active technical threads over a complete archive.</p>
      {% include social.html %}
    </div>
  </div>
</div>

<div class="tabbar">
  <a class="tab" href="/">home.sh</a>
  <a class="tab active" href="/projects/">projects.sh</a>
  <a class="tab" href="/blog/">blog.sh</a>
  <a class="tab" href="/writing/">writing.sh</a>
  <a class="tab" href="/cv/">cv.sh</a>
</div>

## Math, computation, and formal experiments

- [LeanFrontier](https://carlok.github.io/LeanFrontier/) — open Lean 4 library of machine-generated, kernel-verified mathematics on Mathlib.
- [platosdf](https://github.com/carlok/platosdf) — genetic evolver for invariant signed-distance-field solids.
- [erdos-straus-offset-lean](https://github.com/carlok/erdos-straus-offset-lean) — Lean 4-verified fixed-divisor offset construction for 4/n = 1/x + 1/y + 1/z (not a proof of Erdős–Straus).
- [inversive-geometry-lean](https://github.com/carlok/inversive-geometry-lean) — generalized circles (circlines) in Lean 4: circles and lines as one object, cut out by a Hermitian equation.
- [magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean) — Lean 4 on ETP law 1518: one-generated (1518+3862)-magmas are trivial or the Z/3 shift, and constant-coefficient magma cohomology cannot refute 1518 ⇒ 47/614/817/3862.
- [moebius-transcendental-lean](https://github.com/carlok/moebius-transcendental-lean) — Lean 4 formalization of the conjugation degree on the transcendental locus (companion to p19), archived with a Zenodo DOI.
- [unstated-conclusions](https://github.com/carlok/unstated-conclusions) — the dual of unused-assumptions: Mathlib theorems whose proofs establish a stronger conclusion than they state, read off the last step of the proof term.
- [sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean) — Lean 4 formalization of sharp symmetry bounds for real plane algebraic curves: for an irreducible, non-circular real plane curve of degree d, the Euclidean symmetry group is finite, its rotation part cyclic of order at most max(d, 2d−4) and the full group of order at most 2d, with both bounds attained in every degree.
- [unused-assumptions](https://github.com/carlok/unused-assumptions) — Mathlib theorems whose stated typeclass setting is stronger than their proof needs; machine-found one-binder weakenings, each re-verified by the compiler at a pinned Mathlib revision.
- [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) — Lean 4 formalization of a negative result on Diaz's modulus conjecture: a candidate's conjugate is a rational function of it, so no algebraic-hull matrix statement can separate it from an ordinary complex number.
- [aristowrap](https://github.com/carlok/aristowrap) — Docker-first CLI around Harmonic Aristotle, Lean 4, and Mathlib.
- [lean-corpus-density](https://github.com/carlok/lean-corpus-density) — dependency density in Lean 4 corpora, human and machine-generated, with evidence that machine mathematics accumulates. Reproducible from file headers.
- [quadratula](https://github.com/carlok/quadratula) — how much of Le Floch's implication semilattice of Schröder's 990 quasigroup laws small quasigroups already witness: exhaustive enumeration to order 6, exact results to order 9, a provably optimal 17-quasigroup cover, and a generated report with independent checks.
- [prove2me-logs](https://github.com/carlok/prove2me-logs) — working log of Prove2Me formalization activity: per-mission entries with theorem uuids, Lean environments, and what remains open; a record of the work, not an archive of the proofs.
- [euclean](https://github.com/carlok/euclean) — can a machine recover mathematical structure from an anonymized formal theory and a proof checker alone?
- [parsimagma](https://github.com/carlok/parsimagma) — magma signature and coverage engine over the Equational Theories Project law set.
- [dratify](https://github.com/carlok/dratify) — in-process DRAT/DRUP unsatisfiability proof checker for Python and Rust: zero dependencies, with an optional Rust accelerator.
- [cdclkit](https://github.com/carlok/cdclkit) — readable, self-checking CDCL SAT solver, preprocessor, and encoding library: every answer comes with a certificate (models re-checked, UNSAT backed by a DRAT proof an independent checker replays).
- [best-of-lean4](https://github.com/carlok/best-of-lean4) — curated list of awesome Lean 4 projects.
- [modular-zeta3-acceleration](https://github.com/carlok/modular-zeta3-acceleration) — SageMath pipeline for Apéry-type zeta(3) acceleration.

## Infrastructure, security, and operational tools

- [forgepulse](https://github.com/carlok/forgepulse) — self-hosted GitHub traffic-history analytics: Rust, Svelte, SQLite, and Podman.
- [portcullis](https://github.com/carlok/portcullis) — two-phase hardened Ubuntu 26.04 VM provisioner for Hetzner Cloud: ~30-second lockdown first, then a full CIS-style hardening pass, verified by 58 checks.
- [pacenotch](https://github.com/carlok/pacenotch) — Claude usage limits in the terminal, a tray icon and a window: a vertical notch on each bar marks where an even pace would leave you, so the fill says ahead-of-pace or room-to-spare at a glance.
- [python-hosts-checker](https://github.com/carlok/python-hosts-checker) — AWS Lambda endpoint and certificate monitor with Telegram alerts.
- [cold-path-server-podman](https://github.com/carlok/cold-path-server-podman) — run the Cold Path game server (jalhund/cold-path-server) in a Podman container.
- [fleetlens](https://github.com/carlok/fleetlens) — agentless, read-only health reports for a small Debian/Ubuntu VM fleet: Ansible over SSH, Python reports, optional email.
- [Ubuntu-Hardening](https://github.com/carlok/Ubuntu-Hardening) — forked Ubuntu 24.04 CIS hardening script reference.
- [dash](https://github.com/carlok/dash) — serverless DMARC aggregate-report parser for Gmail: extracts, parses, enriches failing sources, emails a summary.
- [sa-client-docker](https://github.com/carlok/sa-client-docker) — SQL Anywhere client container setup with a Python connectivity test.

## Visual and interactive systems

- [neon-bumper-cars](https://github.com/carlok/neon-bumper-cars) — multiplayer WebSocket party game for live events.
- [deck-lovers](https://github.com/carlok/deck-lovers) — Markdown-to-HTML deck with live audience likes and projector sync.
- [agility-trainer](https://github.com/carlok/agility-trainer) — mobile-first bodyweight agility trainer.
- [spriter](https://github.com/carlok/spriter) — browser-only tool that turns a raster image into a pixel-art sprite. No upload, no build, no dependencies.
- [solids-hunter](https://github.com/carlok/solids-hunter) — first-person boolean-rule hunt: Babylon.js game with gamepad support and a shadow-pass watchdog.
- [lifechess](https://github.com/carlok/lifechess) — chess-adjacent experiment mixing game structure and life-state modeling.
- [cross-tetris](https://github.com/carlok/cross-tetris) — shared-queue 4-well cross variant of Tetris: Rust/WASM engine with a rule-based AI, played in the browser.
- [collective-canvas-3d](https://github.com/kiwifarmit/collective-canvas-3d) — collaborative 3D painting app where phones act as brushes.

## Agents, automation, and review workflows

- [topshift-trend](https://github.com/carlok/topshift-trend) — Telegram bot that watches new entries in GitHub monthly trending repositories.
- [caciarabot](https://github.com/carlok/caciarabot) — Italian-first, self-hosted reactive Telegram group bot.
- [llm-source-security-review](https://github.com/carlok/llm-source-security-review) — Codex skill and playbook for defensive source-code security reviews.
- [they-live-agent](https://github.com/carlok/they-live-agent) — local AR-style field-agent scanner experiment inspired by visual overlays.

## Writing, philosophy, and structured notes

- [WIP articles and book PDFs](/book/pdfs/) — generated PDFs for the current book and standalone articles.
