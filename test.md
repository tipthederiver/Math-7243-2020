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
<ul>
{% for sec in site.data.samplelist.mypages %}
{% if sec.audience == "writers" %}
<li>{{sec.url}}</li>
{% endif %}
{% endfor %}
</ul>
