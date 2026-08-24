---
title: Carlo Perassi — software, science, systems
section: home
permalink: /
---

<div class="window">
  <div class="titlebar">
    <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
    <span class="filename">carlok — zsh — 88×30</span>
  </div>
  <div class="pane">
    <p class="prompt">$ <b>whoami</b></p>
    <h1 class="hero-title">Carlo Perassi<span class="cursor"></span></h1>
    <p class="tagline">
      A GitHub-facing hub: a compact map of software systems, scientific computing
      experiments, research notes, and working drafts.
    </p>
  </div>
</div>

<div class="tabbar">
  <a class="tab active" href="/">home.sh</a>
  <a class="tab" href="/projects/">projects.sh</a>
  <a class="tab" href="/writing/">writing.sh</a>
  <a class="tab" href="/blog/">blog.sh</a>
</div>

<p class="cmd">ls ./</p>
<ul class="tree">
  <li><a href="/projects/">projects/</a> — a curated atlas of public GitHub work</li>
  <li><a href="/writing/">writing/</a> — working drafts, article PDFs, and book material</li>
  <li><a href="/blog/">blog/</a> — a public log of activity across my repositories</li>
</ul>

<p class="cmd">cat featured.txt</p>
<div class="feature">
  <div class="label">Featured project</div>
  <h3>LeanFrontier</h3>
  <p>
    An open Lean 4 library of machine-generated, kernel-verified mathematics,
    built on Mathlib. Every contribution is accepted by its mechanically checked
    properties, not by a human explanation of its proof.
  </p>
  <a href="https://carlok.github.io/LeanFrontier/">open carlok.github.io/LeanFrontier →</a>
</div>

<p class="cmd">cat threads.txt</p>
<ul class="tree">
  <li>software systems that are small enough to understand and useful enough to run</li>
  <li>machine learning, distributed computing, agents, and source-code review workflows</li>
  <li>mathematical and computational sketches where code, diagrams, and text share the same page</li>
  <li>public notes that can become articles, talks, tools, or book chapters</li>
</ul>

<p class="cmd">ls _posts/ | head -3</p>
{% for post in site.posts limit:3 %}
<div class="post-card">
  <div class="post-meta"><time>{{ post.date | date: "%Y-%m-%d" }}</time></div>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <div class="excerpt">{{ post.excerpt }}</div>
</div>
{% endfor %}
<p><a href="/blog/">cat _posts/ (all posts) →</a></p>

<p class="cmd">cat README.md</p>
<div class="feature">
  <div class="label">Why this site exists</div>
  <p>
    The personal site answers "who is Carlo?". This site answers "what is Carlo
    building, testing, reading, or formalizing on GitHub?". It is intentionally a
    map, not a portfolio brochure: many entries are experiments, notebooks, drafts,
    or narrow tools.
  </p>
  <ul class="tree">
    <li><a href="https://carlo.perassi.com/">carlo.perassi.com</a> — personal identity page</li>
    <li><a href="https://carlo.perassi.com/cv/">carlo.perassi.com/cv</a> — short CV</li>
    <li><a href="https://github.com/carlok">github.com/carlok</a> — GitHub profile</li>
  </ul>
</div>
