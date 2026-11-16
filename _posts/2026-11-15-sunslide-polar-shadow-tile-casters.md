---
title: "sunslide: the dark band down the planet was polar decor casting a pole-wide shadow, not the tiles"
date: 2026-11-15
tags: [games, project]
---

Playing [sunslide](https://github.com/carlok/sunslide) with shadows on Medium or High and a low sun behind the planet put a huge dark band from the north pole down the face. The measurement is what identified it: at a fixed grazing-sun pose, about 50 % of the centre-column pixels fell below a luminance threshold, the share dropped to 1 % with `polarDecor`'s `castShadow` off, and stayed at 38 % with the tile wall and slab batches' casting disabled — so the north-cap instanced trees and rocks were the caster and the tile shadow pass was legitimate ([#44](https://github.com/carlok/sunslide/pull/44), [611b550](https://github.com/carlok/sunslide/commit/611b550)).

The fix keeps polar decor out of the shadow pass and restores wall and slab casting on the tile `BatchedMesh`, with a separate `customDepthMaterial` per batch, since sphere-mapped tile batches in Three.js r160 produce planet-scale artifacts when casting with one shared material ([23d295e](https://github.com/carlok/sunslide/commit/23d295e), [905e0ff](https://github.com/carlok/sunslide/commit/905e0ff)). The shadow map is refreshed on play and menu transitions and on resume from pause, and the win screen joins the refresh policy. The one-off capture and bisect scripts with host-specific defaults are gone, replaced by `scripts/shadow-repro.mjs`, which reproduces the pose headlessly against the production preview and writes to `tests/out/shadow-pole-graze.png` with `SHADOW_REPRO_*` and `PREVIEW_*` overrides ([aaf05dd](https://github.com/carlok/sunslide/commit/aaf05dd)).
