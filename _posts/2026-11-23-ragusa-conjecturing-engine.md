---
title: "ragusa is public: a conjecturing engine whose output includes the floor it stands on"
date: 2026-11-23
tags: [math, research, rust]
---

[ragusa](https://github.com/carlok/ragusa) went public on 23 November, Apache-2.0, and asks a narrower question than a conjecturing program usually does: not only what it found but what its filters threw away. Every run emits each filter's partition — representative, alias, discarded — with per-object attribution, a chance baseline and a pinning block, and a surviving statement is called a conjecture rather than a theorem, since the engine proves nothing ([13c95ef](https://github.com/carlok/ragusa/commit/13c95ef)).

It has two halves. Project A, in `calibration/`, calls the shipped TxGraffiti 0.4.1 filters and AutoGraphForge's novelty filter as they are and measures what they discard on `graph_data`. Project B, in `engine/`, is a Rust engine over one table type — a dense numeric block and a bit-packed boolean block — that enumerates bounds `target <= c·feature + k` under a hypothesis and implications P ⇒ Q, and runs on TxGraffiti snapshot tables and on parsimagma's magma corpus against the ETP implication graph, a corpus where the answers are already known. The gates and their outcomes live in `CONTROLS.md`, so the controls stay with the core and not only with the validation suite.

The provenance rules are part of the design: the ETP data is Apache-2.0 with attribution in `NOTICE` and hashes in `PROVENANCE.txt`, TxGraffiti and AutoGraphForge are cloned separately and credited in `ACKNOWLEDGMENTS.md` rather than shipped, and KnotInfo is read from knotinfo.org and never bundled, because its maintainers asked that copies not be reposted — results record the sha256 of the file they were computed on. The name follows the same chain the field does: the Dalmatian heuristic is named after the dog, the dog after Dalmatia, and the great city-state of Dalmatia was the Republic of Ragusa.
