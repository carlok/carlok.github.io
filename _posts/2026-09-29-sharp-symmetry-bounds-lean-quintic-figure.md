---
title: "sharp-symmetry-bounds-lean shows the extremal quintic"
date: 2026-09-29
tags: [lean4, math, project]
---

[sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean)
now carries the equality case in the README instead of only in the statement:
a [figure and its drawing script](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/26deee2)
for `Re(z^3(|z|^2 + i)) = 0`, the `d = 5` member of the extremal family, which
has six rotations — the maximum `2d - 4` — plus a view of its complex points.
The script pins numpy and matplotlib inline and runs with
`uv run figures/quintic.py`. No Lean file, challenge, solution, comparator or
registry configuration changed, so the registered commit is unaffected.
