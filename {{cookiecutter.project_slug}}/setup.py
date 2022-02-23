import codecs
from os.path import abspath, dirname, join
from typing import List

from setuptools import find_packages, setup


TEST_DEPS = ["coverage[toml]", "pytest", "pytest-cov"]
DOCS_DEPS = ["sphinx", "sphinx-rtd-theme", "sphinx-autoapi", "recommonmark"
{%- if cookiecutter.is_executable == "yes" %}, "sphinxcontrib-runcmd"]{% else -%}]{% endif %}
CHECK_DEPS = ["isort[colors]", "flake8", "flake8-quotes", "pep8-naming", "mypy", "black"]
REQUIREMENTS: ["loguru"]

EXTRAS = {
    "test": TEST_DEPS,
    "docs": DOCS_DEPS,
    "check": CHECK_DEPS,
    "dev": TEST_DEPS + DOCS_DEPS + CHECK_DEPS,
}

# Read in the version
with open(join(dirname(abspath(__file__)), "VERSION")) as version_file:
    version = version_file.read().strip()


setup(
    name="{{cookiecutter.project_name}}",
    version=version,
    description="{{cookiecutter.project_short_description}}",
    long_description=codecs.open("README.md", "r", "utf-8").read(),
    long_description_content_type="text/markdown",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    url="https://github.com/fchorney/{{cookiecutter.project_slug}}",
    packages=find_packages(exclude=["tests"]),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ],
    platforms=["any"],
    include_package_data=True,
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,{%- if cookiecutter.is_executable == "yes" %}
    entry_points={"console_scripts": ["test_cli = {{cookiecutter.project_slug}}.template:main"]},{%- endif %}
)
