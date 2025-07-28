#!/usr/bin/env python3
"""
Write a type-annotated function concat that takes a string str1
and a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Write a type-annotated function concat that takes a string str1 and
    a string str2 as arguments and returns a concatenated string

    Args:
        str1 (str): string
        str2 (str): string

    Returns:
        str: string
    """
    str3 = str1 + str2
    return str3
