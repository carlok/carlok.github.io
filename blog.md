---
title: Blog
section: blog
permalink: /blog/
---

<div class="window">
  <div class="titlebar">
    <div class="dot r"></div><div class="dot y"></div><div class="dot g"></div>
    <span class="filename">carlok — zsh — 88×30</span>
  </div>
  <div class="pane hero-split">
    <img class="avatar" src="https://github.com/carlok.png?size=460" alt="Carlo Perassi">
    <div class="hero-body">
      <p class="prompt">$ <b>cat blog/README.md</b></p>
      <h1 class="hero-title">Blog<span class="cursor"></span></h1>
      <p class="tagline">A public log of what's changing across my repositories — releases, meaningful commits, and new projects. Only public activity appears here; routine chores, typo fixes, and automated merge noise are left out.</p>
      {% include social.html %}
    </div>
  </div>
</div>

<div class="tabbar">
  <a class="tab" href="/">home.sh</a>
  <a class="tab" href="/projects/">projects.sh</a>
  <a class="tab active" href="/blog/">blog.sh</a>
  <a class="tab" href="/writing/">writing.sh</a>
  <a class="tab" href="/cv/">cv.sh</a>
</div>

<p class="cmd">ls _posts/</p>
{% for post in site.posts %}
<div class="post-card">
  <div class="post-meta">
    <time>{{ post.date | date: "%Y-%m-%d" }}</time>
    {% for tag in post.tags %}<a class="badge" href="{{ '/blog/tag/' | append: tag | append: '/' | relative_url }}">{{ tag }}</a>{% endfor %}
  </div>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <div class="excerpt">{{ post.excerpt }}</div>
</div>
{% endfor %}
