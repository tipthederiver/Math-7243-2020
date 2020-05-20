---
layout     : default
---

# Test

{% for author in authors %}
    Username: {{ author[0] }}
    Full Name: {{ author[1]["name"] }}
    {% if author[1]["site"] != "" %}
        Site: {{ author[1]["site"] }}
    {% endif %}
    E-Mail: {{ author[1]["email"] }}
    -----
{% endfor %}

# Did it work?
