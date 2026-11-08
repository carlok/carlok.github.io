---
title: "guess-the-move is public: a chess trainer that shows what Stockfish, a real player and Maia would do"
date: 2026-11-07
tags: [games, project]
---

[guess-the-move](https://github.com/carlok/guess-the-move) went public on 7 November and plays at [carlok.github.io/guess-the-move](https://carlok.github.io/guess-the-move/): a position comes up, you guess a move, and the app reveals three references and how far your guess is from each on a normalized scale — Stockfish's best move, the move a real player of known rating actually played, and Maia's move at that rating. The shipped set is 2,000 real positions from Lichess standard rated games of September 2026 (CC0), players rated 1200 to 2000, every legal move evaluated by Stockfish 19 at 400,000 nodes and stored with Maia-3 move probabilities; no player names are stored, but each position keeps its Lichess game link so a game can be taken out on request.

The level estimate is computed in the page from your first-time best-move guesses, with no server: each position's Maia probabilities at five rating anchors score your move over a rating grid, and positions where the ratings disagree count for more, measured in bits of mutual information. The README says how far that can be trusted — on real players of known rating the 80% range held the truth about 80% of the time but was 400 to 700 points wide, estimates ran below Lichess Rapid ratings, and players near 1900 came out near 1650, with the evidence in `docs/research/level-eval.json` and the script that reproduces it. Everything on the page is local: history in `localStorage`, a content policy that allows no request to any other site, and a static page on GitHub Pages.
