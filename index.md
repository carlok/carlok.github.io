---
title: Carlo Perassi — software, science, systems
section: home
permalink: /
---

<div class="hero">
  <p class="eyebrow">Software · Science · Systems</p>
  <h1>Carlo Perassi</h1>
  <p class="tagline">
    A GitHub-facing hub: a compact map of software systems, scientific computing
    experiments, research notes, and working drafts.
  </p>
</div>

<div class="grid cols-3">
  <a class="card" href="/projects/">
    <h3>Projects</h3>
    <p>A curated atlas of public GitHub work.</p>
  </a>
  <a class="card" href="/writing/">
    <h3>Writing</h3>
    <p>Working drafts, article PDFs, and book material.</p>
  </a>
  <a class="card" href="/blog/">
    <h3>Blog</h3>
    <p>A public log of activity across my repositories.</p>
  </a>
</div>

## Featured

<div class="feature">
  <div class="card-meta"><span class="badge">Featured project</span></div>
  <h3>LeanFrontier</h3>
  <p>
    An open Lean 4 library of machine-generated, kernel-verified mathematics,
    built on Mathlib. Every contribution is accepted by its mechanically checked
    properties, not by a human explanation of its proof.
  </p>
  <a class="btn" href="https://carlok.github.io/LeanFrontier/">Open LeanFrontier ↗</a>
</div>

## Current threads

- Software systems that are small enough to understand and useful enough to run.
- Machine learning, distributed computing, agents, and source-code review workflows.
- Mathematical and computational sketches where code, diagrams, and text share the same page.
- Public notes that can become articles, talks, tools, or book chapters.

## Recent posts

{% for post in site.posts limit:3 %}
<div class="post-card">
  <div class="post-meta"><time>{{ post.date | date: "%b %d, %Y" }}</time></div>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="excerpt">{{ post.excerpt | strip_html }}</p>
</div>
{% endfor %}

<p><a href="/blog/">View all posts →</a></p>

## Why this site exists

The personal site answers "who is Carlo?". This site answers "what is Carlo
building, testing, reading, or formalizing on GitHub?". It is intentionally a
map, not a portfolio brochure: many entries are experiments, notebooks, drafts,
or narrow tools.

- [carlo.perassi.com](https://carlo.perassi.com/) — personal identity page
- [carlo.perassi.com/cv](https://carlo.perassi.com/cv/) — short CV
- [github.com/carlok](https://github.com/carlok) — GitHub profile
