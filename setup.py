from setuptools import setup


TEST_DEPS = ["pytest", "pytest-cookies", "flake8", "tox"]
CHECK_DEPS = [
    "isort[colors]",
    "black",
    "flake8",
    "flake8-quotes",
    "pep8-naming",
    "mypy",
]
REQUIREMENTS = ["cookiecutter", "jinja2-time"]

EXTRAS = {"test": TEST_DEPS, "check": CHECK_DEPS, "dev": TEST_DEPS + CHECK_DEPS}

setup(
    name="cookiecutter-fchorney",
    version="0.1.0",
    description="CookieCutter template for my personal python projects",
    author="Fernando Chorney",
    author_email="github@djsbx.com",
    url="https://github.com/fchorney/cookiecutter-fchorney",
    packages=[],
    install_requires=REQUIREMENTS,
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,
)
