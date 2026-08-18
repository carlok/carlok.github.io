---
title: Blog
section: blog
permalink: /blog/
---

# Blog

A public log of what's changing across my repositories — releases, meaningful
commits, and new projects. Only public activity appears here; routine chores,
typo fixes, and automated merge noise are left out.

{% for post in site.posts %}
<div class="post-card">
  <div class="post-meta">
    <time>{{ post.date | date: "%b %d, %Y" }}</time>
    {% for tag in post.tags %}<span class="badge neutral">{{ tag }}</span>{% endfor %}
  </div>
  <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
  <p class="excerpt">{{ post.excerpt | strip_html }}</p>
</div>
{% endfor %}
