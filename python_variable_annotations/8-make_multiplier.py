#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a float
by multiplier.

Returns:
    _type_: function
"""
import typing

def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Write a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier.

    Args:
        multiplier (float): float

    Returns:
        typing.Callable[[float], float]: fonction qui prend deux float
    """
    def multiply(value: float) -> float:
        """Write a type-annotated function make_multiplier that takes a
        float multiplier as argument and returns a function that multiplies
        a float by multiplier.

        Args:
            value (float): float

        Returns:
            float: float
        """
        result = multiplier * value
        return result
    return multiply
