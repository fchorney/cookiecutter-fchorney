{% if cookiecutter.is_executable == "yes" %}import argparse
from typing import Optional, Sequence
{% endif -%}from loguru import logger


def function_test(x: int) -> int:
    """
    Returns the input value multiplied by 2

    Args:
        x (int): Value to multiply

    Returns:
        int: input value multiplied by 2

    Example:
        >>> function_test(2)
        4
    """
    return x * 2
{%- if cookiecutter.is_executable == "yes" %}


def main(args: Optional[Sequence[str]] = None):
    pargs = parse_args(args=args)


def parse_args(args: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="{{cookiecutter.project_short_description}}")

    parser.add_argument("someargument", help="argument help")

    return parser.parse_args(args)


if __name__ == "__main__":
    main(){% endif %}
