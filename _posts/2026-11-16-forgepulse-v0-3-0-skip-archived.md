---
title: "forgepulse 0.3.0: the dashboard can leave archived repositories out of every number"
date: 2026-11-16
tags: [tool, project]
---

[forgepulse](https://github.com/carlok/forgepulse) 0.3.0 adds a **Skip archived** checkbox next to the search box, and the exclusion happens on the server rather than in the view: with it ticked, ranks, shares, trend arrows, the KPI totals, the charts and the JSONL export are all computed without archived repositories instead of archived rows being hidden after the fact ([v0.3.0](https://github.com/carlok/forgepulse/releases/tag/v0.3.0), [e19c2c7](https://github.com/carlok/forgepulse/commit/e19c2c7)). The choice is remembered per browser and off by default, `GET /api/v1/dashboard` and `GET /api/v1/export.jsonl` accept `include_archived=false`, and the stars feed still lists stars on archived repositories — a star given before a repository was archived is still a star. It is the first feature release since [0.2.0 moved production to Distroless](/blog/2026/10/29/forgepulse-v0-2-0-distroless/).
