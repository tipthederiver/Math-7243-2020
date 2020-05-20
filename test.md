---
layout     : default
---

# Test
<ul>
    {% for project in site.data.projects.projects %}
        <li>{{project.title}}</li>
        <li>{{project.names}}</li>
        <li>{{project.thumb-url}}</li>
    {% endfor %}
</ul>

# Did it work?
<ul>
{% for sec in site.data.samplelist.mypages %}
{% if sec.audience == "writers" %}
<li>{{sec.url}}</li>
{% endif %}
{% endfor %}
</ul>
