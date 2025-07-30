#!/usr/bin/env python3
import typing

def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    def multiply(value: float) -> float:
        result = multiplier * value
        return result
    return multiply
