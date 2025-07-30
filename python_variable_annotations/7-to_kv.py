#!/usr/bin/env python3
"""
Write a type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple. The first element of the
tuple is the string k. The second element is the square of the int/float v
and should be annotated as a float.
Returns:
    _type_: return str anf float
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Write a type-annotated function to_kv that takes a string k and an
    int OR float v as arguments and returns a tuple. The first element of the
    tuple is the string k. The second element is the square of the int/float v
    and should be annotated as a float.

    Args:
        k (str): string
        v (typing.Union[int, float]): float ou int

    Returns:
        typing.Tuple[str, float]: return string and float
    """
    return (k, v*v)
