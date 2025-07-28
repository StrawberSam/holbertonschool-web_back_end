#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.

Returns:
_type_: the sum of the list as a float
"""
from math import *
import typing
from typing import Union


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
Write a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.

    Args:
        mxd_lst (typing.List[typing.Union[int, float]]): list of int and float

    Returns:
        float: the sum of the list as a float
    """
    return sum(mxd_lst)
