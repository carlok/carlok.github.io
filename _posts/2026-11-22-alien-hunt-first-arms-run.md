---
title: "alien-hunt ran --arms for the first time: joserfc's DoS advisory confirmed, a second claim made and not confirmed"
date: 2026-11-22
tags: [security, tool]
---

The README of [alien-hunt](https://github.com/carlok/alien-hunt) said `--arms` had never been run. It has now, once: joserfc at `26a10275`, the parent of its first DoS fix, under alien-hunt 0.2.0 with Claude Sonnet 5.5 through Anthropic's OpenAI-compatible endpoint, for 1.43 USD and nothing cut short ([PR #13](https://github.com/carlok/alien-hunt/pull/13)).

The result is a confirmation rather than a discovery. The directed hunt confirmed GHSA-jpxq-7h8p-2q76 — 200,000 recipients all processed by `extract_general_json` — the first time either joserfc advisory has been confirmed by the tool, and `alien-hunt replay --against d6dc8df`, the advisory's own fix, refuses the claim, so it is specific to the defect; the advisory was public before the run, so the model may have known about it. GHSA-9pg5-8c7x-5hfx was claimed and not confirmed, and AH-1 and AH-4 still fire on upstream `e65b379`, named by alias and class only, undecided.

Does the score choose anything? The per-rule tally of real issues is 1 combined, 3 coherence, 2 random across 30 picks and 20 distinct candidates, three of them shared by every rule — and the advisory claim came from one of those three. The six hunt claims were labelled blind by a separate model reviewer working from the shuffled label sheet and the library source at the commit, not by a person, and one of the "real issues" is a claim the check refused.
