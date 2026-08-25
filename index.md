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
  <div class="pane hero-split">
    <img class="avatar" src="https://github.com/carlok.png?size=460" alt="Carlo Perassi">
    <div class="hero-body">
      <p class="prompt">$ <b>whoami</b></p>
      <h1 class="hero-title">Carlo Perassi<span class="cursor"></span></h1>
      <p class="tagline">
        A GitHub-facing hub: a compact map of software systems, scientific computing
        experiments, research notes, and working drafts.
      </p>
      {% include social.html %}
    </div>
  </div>
</div>

<div class="tabbar">
  <a class="tab active" href="/">home.sh</a>
  <a class="tab" href="/projects/">projects.sh</a>
  <a class="tab" href="/blog/">blog.sh</a>
  <a class="tab" href="/writing/">writing.sh</a>
  <a class="tab" href="/cv/">cv.sh</a>
</div>

<p class="cmd">ls ./</p>
<ul class="tree">
  <li><a href="/projects/">projects/</a> — a curated atlas of public GitHub work</li>
  <li><a href="/writing/">writing/</a> — working drafts, article PDFs, and book material</li>
  <li><a href="/blog/">blog/</a> — a public log of activity across my repositories</li>
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
  <p>
    That personal identity page is at <a href="https://carlo.perassi.com/">carlo.perassi.com</a>.
  </p>
</div>
