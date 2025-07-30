#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values
with the appropriate types

Returns:
    _type_: _description_
"""
import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Annotate the below function’s parameters and return values with the
    appropriate types

    Args:
        lst (typing.Iterable[typing.Sequence]): _description_

    Returns:
        typing.List[typing.Tuple[typing.Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]
