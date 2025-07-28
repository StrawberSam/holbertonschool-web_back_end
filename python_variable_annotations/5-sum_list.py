#!usr/bin/env python3
"""
Write a type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float.

Returns:
    _type_: return sum of the float list
"""
from math import *
import typing

def sum_list(input_list: typing.List[float]) -> float:
    """
    Write a type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float.

    Args:
        input_list (typing.List[float]): list of float

    Returns:
        float: the sum of all the float in the list
    """
    return sum(input_list)
