---
title: "caciarabot: CodeQL's secret-logging alert reopens on a probability, and the fix enumerates the whole config"
date: 2026-11-05
tags: [bot, security]
---

CodeQL alert 1 in [caciarabot](https://github.com/carlok/caciarabot) came back — the `py/clear-text-logging-sensitive-data` finding reopened after the startup log line added on [4 November](/blog/2026/11/04/caciarabot-settings-loaded-stats-rates/), this time tracing `bot_config.llm_secret_probability` into `settings_loaded`. The value is a float; the rule matched the word in its name. Instead of naming fields one at a time, `logging_utils.py` now walks the dataclass with `dataclasses.asdict`, so the whole effective configuration is logged at startup and a field added later is included without anyone remembering to add it ([28b1391](https://github.com/carlok/caciarabot/commit/28b1391)), with a new `tests/test_logging_utils.py` covering the rendering. It is the same false-positive shape as the September `segreto` [count fix](/blog/2026/09/25/caciarabot-secret-log-count/) — a rule named for credentials firing on the word rather than on one — so the enumeration retires the next instance before it is filed.
