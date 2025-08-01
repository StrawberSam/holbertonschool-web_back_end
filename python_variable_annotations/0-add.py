#!/usr/bin/env python3
"""
Write a type-annotated function add that takes a float a and a float b as
arguments and returns their sum as a float.
"""


def add(a: float, b: float) -> float:
    """Write a type-annotated function add that takes a float a and a float
    b as arguments and returns their sum as a float.

    Args:
        a (float): number
        b (float): number

    Returns:
        float: type
    """
    result = (a, b)
    return sum(result)
