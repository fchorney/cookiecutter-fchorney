## Template

Explain Template Here
{% if cookiecutter.is_executable == "yes" %}
### Usage

```eval_rst
.. runcmd:: python ./{{cookiecutter.project_slug}}/template.py --help
   :syntax: sh
   :prompt:
```{% endif %}
