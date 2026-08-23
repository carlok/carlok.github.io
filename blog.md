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
  <div class="pane">
    <p class="prompt">$ <b>cat blog/README.md</b></p>
    <h1 class="hero-title">Blog</h1>
    <p class="tagline">A public log of what's changing across my repositories — releases, meaningful commits, and new projects. Only public activity appears here; routine chores, typo fixes, and automated merge noise are left out.</p>
  </div>
</div>

<div class="tabbar">
  <a class="tab" href="/">home.sh</a>
  <a class="tab" href="/projects/">projects.sh</a>
  <a class="tab" href="/writing/">writing.sh</a>
  <a class="tab active" href="/blog/">blog.sh</a>
</div>

<p class="cmd">ls _posts/</p>
{% for post in site.posts %}
<div class="post-card">
  <div class="post-meta">
    <time>{{ post.date | date: "%b %d, %Y" }}</time>
    {% for tag in post.tags %}<a class="badge" href="{{ '/blog/tag/' | append: tag | append: '/' | relative_url }}">{{ tag }}</a>{% endfor %}
  </div>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="excerpt">{{ post.excerpt | strip_html }}</p>
</div>
{% endfor %}
