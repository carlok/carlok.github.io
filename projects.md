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
  <a class="tab" href="/math/">math.sh</a>
  <a class="tab" href="/cv/">cv.sh</a>
</div>

## Math, computation, and formal experiments

- [prove2me-logs](https://github.com/carlok/prove2me-logs) — working log of Prove2Me formalization activity: per-mission entries with theorem uuids, Lean environments, and what remains open; a record of the work, not an archive of the proofs.
- [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) — Lean 4 formalization of a negative result on Diaz's modulus conjecture: a candidate's conjugate is a rational function of it, so no algebraic-hull matrix statement can separate it from an ordinary complex number.
- [LeanFrontier](https://github.com/carlok/LeanFrontier) — open Lean 4 library of machine-generated, kernel-verified mathematics on Mathlib.
- [lspace-det-sigma](https://github.com/carlok/lspace-det-sigma) — an inequality between determinant and signature for L-space knots: the note, its computations, and a Lean 4 proof of the lattice lemma.
- [aristowrap](https://github.com/carlok/aristowrap) — Docker-first CLI around Harmonic Aristotle, Lean 4, and Mathlib.
- [dratify](https://github.com/carlok/dratify) — in-process DRAT/DRUP unsatisfiability proof checker for Python and Rust: zero dependencies, with an optional Rust accelerator.
- [cdclkit](https://github.com/carlok/cdclkit) — readable, self-checking CDCL SAT solver, preprocessor, and encoding library: every answer comes with a certificate (models re-checked, UNSAT backed by a DRAT proof an independent checker replays).
- [quadratula](https://github.com/carlok/quadratula) — how much of Le Floch's implication semilattice of Schröder's 990 quasigroup laws small quasigroups already witness: exhaustive enumeration to order 6, exact results to order 9, a provably optimal 17-quasigroup cover, and a generated report with independent checks.
- [platosdf](https://github.com/carlok/platosdf) — genetic evolver for invariant signed-distance-field solids.
- [curve-symmetry-lean](https://github.com/carlok/curve-symmetry-lean) — the note *Sharp symmetry bounds for real algebraic curves* (PDF and TeX) with a Lean 4 port that checks every theorem, lemma and remark of it: an irreducible, non-circular real plane curve of degree d has at most max(d, 2d−4) rotations and at most 2d Euclidean symmetries, both sharp in every degree, plus the d ≥ 5 classification of the extremal family and its exact ambient Möbius groups.
- [consilean](https://github.com/carlok/consilean) — scores pairs of formal Lean statements by similarity and dependency-graph distance: similar-and-near pairs are duplicate candidates, similar-and-far pairs are candidate hidden connections, and the kernel decides whether a connection holds.
- [magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean) — Lean 4 on ETP law 1518: one-generated (1518+3862)-magmas are trivial or the Z/3 shift, and constant-coefficient magma cohomology cannot refute 1518 ⇒ 47/614/817/3862.
- [sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean) — Lean 4 formalization of sharp symmetry bounds for real plane algebraic curves: for an irreducible, non-circular real plane curve of degree d, the Euclidean symmetry group is finite, its rotation part cyclic of order at most max(d, 2d−4) and the full group of order at most 2d, with both bounds attained in every degree.
- [unstated-conclusions](https://github.com/carlok/unstated-conclusions) — the dual of unused-assumptions: Mathlib theorems whose proofs establish a stronger conclusion than they state, read off the last step of the proof term.
- [erdos-straus-offset-lean](https://github.com/carlok/erdos-straus-offset-lean) — Lean 4-verified fixed-divisor offset construction for 4/n = 1/x + 1/y + 1/z (not a proof of Erdős–Straus).
- [inversive-geometry-lean](https://github.com/carlok/inversive-geometry-lean) — generalized circles (circlines) in Lean 4: circles and lines as one object, cut out by a Hermitian equation.
- [moebius-transcendental-lean](https://github.com/carlok/moebius-transcendental-lean) — Lean 4 formalization of the conjugation degree on the transcendental locus (companion to p19), archived with a Zenodo DOI.
- [unused-assumptions](https://github.com/carlok/unused-assumptions) — Mathlib theorems whose stated typeclass setting is stronger than their proof needs; machine-found one-binder weakenings, each re-verified by the compiler at a pinned Mathlib revision.
- [lean-corpus-density](https://github.com/carlok/lean-corpus-density) — dependency density in Lean 4 corpora, human and machine-generated, with evidence that machine mathematics accumulates. Reproducible from file headers.
- [euclean](https://github.com/carlok/euclean) — can a machine recover mathematical structure from an anonymized formal theory and a proof checker alone?
- [parsimagma](https://github.com/carlok/parsimagma) — magma signature and coverage engine over the Equational Theories Project law set.
- [best-of-lean4](https://github.com/carlok/best-of-lean4) — curated list of awesome Lean 4 projects.
- [modular-zeta3-acceleration](https://github.com/carlok/modular-zeta3-acceleration) — SageMath pipeline for Apéry-type zeta(3) acceleration.

## Infrastructure, security, and operational tools

- [pacenotch](https://github.com/carlok/pacenotch) — Claude usage limits in the terminal, a tray icon and a window: a vertical notch on each bar marks where an even pace would leave you, so the fill says ahead-of-pace or room-to-spare at a glance.
- [hermes-podman](https://github.com/carlok/hermes-podman) — headless Hermes Agent gateway on rootless Podman: image pinned by tag and digest, Makefile and scripts for setup, backup, restore, upgrade and uninstall, reboot survival, CI-exercised on Ubuntu 26.04.
- [forgepulse](https://github.com/carlok/forgepulse) — self-hosted GitHub traffic-history analytics: Rust, Svelte, SQLite, and Podman.
- [matrix-podman-stack](https://github.com/carlok/matrix-podman-stack) — private Matrix homeserver on rootless Podman: Synapse and Postgres, Element Web, an optional Telegram bridge, optional Prometheus/Grafana, NATS and Valkey as a bot bus, all bind-mounted under one `DATA_DIR` and publishing on `127.0.0.1` only, with the bot accounts driven by a `bots.yaml` file.
- [fleetlens](https://github.com/carlok/fleetlens) — agentless, read-only health reports for a small Debian/Ubuntu VM fleet: Ansible over SSH, Python reports, optional email.
- [portcullis](https://github.com/carlok/portcullis) — two-phase hardened Ubuntu 26.04 VM provisioner for Hetzner Cloud: ~30-second lockdown first, then a full CIS-style hardening pass, verified by 58 checks.
- [python-hosts-checker](https://github.com/carlok/python-hosts-checker) — AWS Lambda endpoint and certificate monitor with Telegram alerts.
- [sa-client-docker](https://github.com/carlok/sa-client-docker) — SQL Anywhere client container setup with a Python connectivity test.
- [dash](https://github.com/carlok/dash) — serverless DMARC aggregate-report parser for Gmail: extracts, parses, enriches failing sources, emails a summary.
- [cold-path-server-podman](https://github.com/carlok/cold-path-server-podman) — run the Cold Path game server (jalhund/cold-path-server) in a Podman container.
- [Ubuntu-Hardening](https://github.com/carlok/Ubuntu-Hardening) — forked Ubuntu 24.04 CIS hardening script reference.

## Agents, automation, and review workflows

- [alien-hunt](https://github.com/carlok/alien-hunt) — samples the defects a plain LLM review of a repository does not report, adapting The Alien Space of Science to code: candidates from the library's own sources, sinks and invariants, ranked by a model's coherence rating and by embedding distance from what the reviews already said, confirmed only when a reproducer imports the library, calls the function and exits 0 inside a sandbox.
- [caciarabot](https://github.com/carlok/caciarabot) — Italian-first, self-hosted reactive Telegram group bot.
- [roundstorm](https://github.com/carlok/roundstorm) — local-first app where persistent, heterogeneous AI researchers deliberate for a set number of rounds on a hard question; macOS, Linux and Windows.
- [slop-audit](https://github.com/carlok/slop-audit) — local multi-tool harness for AI-slop and formulaic prose: writing linters, descriptive stats and separate local AI-authorship signals, with no hosted detectors.
- [they-live-agent](https://github.com/carlok/they-live-agent) — local AR-style field-agent scanner experiment inspired by visual overlays.
- [llm-source-security-review](https://github.com/carlok/llm-source-security-review) — Codex skill and playbook for defensive source-code security reviews.
- [topshift-trend](https://github.com/carlok/topshift-trend) — Telegram bot that watches new entries in GitHub monthly trending repositories.

## Visual and interactive systems

- [agility-trainer](https://github.com/carlok/agility-trainer) — mobile-first bodyweight agility trainer.
- [solids-hunter](https://github.com/carlok/solids-hunter) — first-person boolean-rule hunt: Babylon.js game with gamepad support and a shadow-pass watchdog.
- [cross-tetris](https://github.com/carlok/cross-tetris) — shared-queue 4-well cross variant of Tetris: Rust/WASM engine with a rule-based AI, played in the browser.
- [neon-bumper-cars](https://github.com/carlok/neon-bumper-cars) — multiplayer WebSocket party game for live events.
- [staffarda](https://github.com/carlok/staffarda) — procedural Blender reconstruction of the ground floor of the Staffarda Abbey guesthouse, rebuilt from three photos: rib vault, four columns, weathered materials, a two-minute walkthrough, and a first-order thrust-line check of the vault.
- [consculpta](https://github.com/carlok/consculpta) — browser-only breeder of 3D sculptures: formulas over simplex noise, mutated as trees, raymarched in WebGL 2, with a genome editor, Shadertoy export and an optional bring-your-own-key AI co-breeder.
- [lifechess](https://github.com/carlok/lifechess) — chess-adjacent experiment mixing game structure and life-state modeling.
- [deck-lovers](https://github.com/carlok/deck-lovers) — Markdown-to-HTML deck with live audience likes and projector sync.
- [spriter](https://github.com/carlok/spriter) — browser-only tool that turns a raster image into a pixel-art sprite. No upload, no build, no dependencies.
- [collective-canvas-3d](https://github.com/kiwifarmit/collective-canvas-3d) — collaborative 3D painting app where phones act as brushes.

## Writing, philosophy, and structured notes

- [WIP articles and book PDFs](/book/pdfs/) — generated PDFs for the current book and standalone articles.
