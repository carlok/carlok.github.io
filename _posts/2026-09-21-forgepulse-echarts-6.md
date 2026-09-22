---
title: "forgepulse: the echarts 6 bump moved the legend onto the axis labels"
date: 2026-09-21
tags: [rust, tool]
---

The `echarts` 5 → 6 bump in [forgepulse](https://github.com/carlok/forgepulse)
changed the default legend position from top to bottom, so on both charts the
legend collided with the x-axis date labels while the 48px the grid reserves at
the top sat empty — `legend.top` is now set explicitly, so the layout stops
depending on a library default
([94fb8c1](https://github.com/carlok/forgepulse/commit/94fb8c1)). The same release
draws a filled marker on every data point, which on a hundred-day series is
clutter; the dots are hidden on all eight series through one shared base while the
axis tooltip still marks the hovered point
([1f70b65](https://github.com/carlok/forgepulse/commit/1f70b65)). Both rode in with
the `vitest` 4.1.11 / `echarts` 6.1.0 security bump.
