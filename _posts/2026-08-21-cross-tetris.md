---
title: "cross-tetris: a shared-queue four-well Tetris"
date: 2026-08-21
tags: [games, rust, project]
---

[cross-tetris](https://github.com/carlok/cross-tetris) is a new game: four
standard Tetris wells arranged in a cross, sharing a single piece stream. You
— or a greedy rule-based AI — pick which well each piece falls into, the
wells play out as ordinary real-time Tetris, and the game ends when any well
tops out. The engine is Rust compiled to WASM with a React UI, and it is
[playable live](https://carlok.github.io/cross-tetris/).
