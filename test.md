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

# Test 2

<div class="row">
  {% for project in site.data.projects.projects %}
  <div class="column">
    <div class="card">
      <img src="{{project.thumb-url}}" style="width:100%">
      <div class="container">
        <h4><b>{{project.title}}</b></h4>
        <p>{{project.names}}</p>
        <p><a href="{{project.paper-url}}">Paper</a> | <a href="{{project.pres-url}}">Presentation</a> | <a href="{{project.slide-url}}">Slides</a></p>
      </div>
    </div>
  </div>
  {% endfor %}
</div>

# Did it work?
<ul>
{% for sec in site.data.samplelist.mypages %}
{% if sec.audience == "writers" %}
<li>{{sec.url}}</li>
{% endif %}
{% endfor %}
</ul>
