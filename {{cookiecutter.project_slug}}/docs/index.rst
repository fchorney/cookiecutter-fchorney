{{cookiecutter.project_name}}
{{cookiecutter.project_name|length * "="}}

{{cookiecutter.project_short_description}}

.. toctree::
   :maxdepth: 1
   :caption: General
   :name: sec-general

   general/index

.. toctree::
   :maxdepth: 1
   :caption: Code Reference
   :name: sec-code-ref

   autoapi/{{cookiecutter.project_slug}}/index

.. toctree::
   :maxdepth: 1
   :caption: Code Coverage
   :name: sec-code-coverage

   Coverage <./coverage/index.html#http://>
