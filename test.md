---
layout     : default
---

# Test

{% for author in site.authors %}
    Username: {{ author[0] }}
    Full Name: {{ author[1]["name"] }}
    {% if author[1]["site"] != "" %}
        Site: {{ author[1]["site"] }}
    {% endif %}
    E-Mail: {{ author[1]["email"] }}
    -----
{% endfor %}

{% for author in site.author %}
    {{ author }}
    ----
{% endfor %}

# Did it work?
{% for item in site.data.samplelist.toc %}
<h3>{{item.title}}</h3>
<ul>
{% for entry in item.subfolderitems %}
<li>{{entry.page}}</li>
{% endfor %}
</ul>
{% endfor %}
