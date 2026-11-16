---
title: "llm-source-security-review: an evidence bar for findings, a schema gate, and SARIF out"
date: 2026-11-15
tags: [security, tool]
---

[llm-source-security-review](https://github.com/carlok/llm-source-security-review), the playbook and Codex skill for defensive source review, gained the parts that turn a finding into something a tool can check ([#2](https://github.com/carlok/llm-source-security-review/pull/2), [5f8446f](https://github.com/carlok/llm-source-security-review/commit/5f8446f)). `references/standards-grounding.md` maps findings to CWE, OWASP Top 10:2021 and ASVS chapters and sets an evidence bar — source, propagation, sink — before a claim counts, while `references/phase-prompts.md` adds prompt-injection resistance, large-repo chunking, a supply-chain and CI pass, and a PR/diff review mode, and the schemas take optional `cwe_ids`, `owasp_category`, `asvs_refs`, `severity` and a numeric `confidence_score`.

Three scripts carry it: `finding_tools.py` validates the JSONL, dedupes by fingerprint and builds SARIF 2.1.0 with model-derived findings tagged `precision: medium`; `validate_findings.py` is the schema gate, so a positive verdict without evidence or with a short `source_to_sink` or `reasoning_summary` fails; and `export_sarif.py` produces the file a code-scanning upload workflow expects. The repository now runs its own unit tests at a floor of 85 % coverage on `scripts/`, with a smoke test for the validator and the SARIF export, and took the community files the other repositories carry — `AGENT.md`, CONTRIBUTING, Contributor Covenant 2.1, private advisories only in `SECURITY.md`, issue forms, and Dependabot for Actions.
