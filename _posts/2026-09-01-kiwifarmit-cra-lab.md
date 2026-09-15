---
title: "kiwifarmit/cra-lab is public: CI/CD pipelines that produce CRA evidence"
date: 2026-09-01
tags: [security, tool]
---

[kiwifarmit/cra-lab](https://github.com/kiwifarmit/cra-lab) is now public — a
small lab in the Kiwifarm org that builds the pipeline half of a Cyber
Resilience Act story instead of describing it. Pull requests go through Semgrep
SAST plus SCA and IaC scanning (Semgrep rather than CodeQL, which needs GitHub
Advanced Security on private repos, and it runs entirely on the runner so the
code never leaves it); a `v*` tag generates a CycloneDX SBOM with Syft, hashes
it, hands the digest to the SLSA generic generator for provenance, and runs
Trivy over the release SBOM at CRITICAL/HIGH before attaching it to the release
([pr-security.yml](https://github.com/kiwifarmit/cra-lab/blob/main/.github/workflows/pr-security.yml),
[release-security.yml](https://github.com/kiwifarmit/cra-lab/blob/main/.github/workflows/release-security.yml)).
A weekly Trivy and Semgrep sweep covers vulnerability, misconfiguration and
licence scanning on a timer, and Dependabot keeps the actions the workflows
themselves depend on pinned, with each workflow's comments citing the CRA
Annex I Part II clause it answers.
