---
title: "staffarda: the model revised against the photos, and a walkthrough mode that renders the same moment in EEVEE and Cycles"
date: 2026-10-19
tags: [project]
---

The [staffarda](https://github.com/carlok/staffarda) model was revised against the three source photos before the walkthrough was rendered: weathered materials instead of clean ones, wall corbels made higher and smaller, four column bases added, and the large windows kept as they are today with the arched heads left behind a hypothesis switch rather than assumed ([2cc47a3](https://github.com/carlok/staffarda/commit/2cc47a3), [97bb8d5](https://github.com/carlok/staffarda/commit/97bb8d5)) — the same policy as the rest of the reconstruction, where what the photos show and what the literature suggests are separate settings.

`blender/walkthrough.py` gained a `compare` mode: eight named moments — the doorway, the ribs and keystone, walking under the vault, the doorways and corbel beside column 3, and the rest of the route — rendered as stills in both engines, with Cycles at a chosen sample count and motion blur on, into `tmp/high_compare/` ([697dbaa](https://github.com/carlok/staffarda/commit/697dbaa)). It was added for a concrete reason: the earlier take had springer blocks narrower than the arch they sit on, so the render flickered there, and the fix widens them past the arch sides ([cad4aaf](https://github.com/carlok/staffarda/commit/cad4aaf)).
