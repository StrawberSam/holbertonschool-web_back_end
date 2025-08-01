#!/usr/bin/env python
"""
Import wait_random from the previous python file that you’ve written and
write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times with
the specified max_delay.

wait_n should return the list of all the delays (float values). The list of
the delays should be in ascending order without using sort() because of
concurrency.

Returns:
    _type_: list of float
"""
import asyncio
import typing


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Import wait_random from the previous python file that you’ve written and
    write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times with
    the specified max_delay.

    wait_n should return the list of all the delays (float values). The list of
    the delays should be in ascending order without using sort() because of
    concurrency.

    Args:
        n (int): number of time
        max_delay (int): nuùber

    Returns:
        typing.List[float]: list of float
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    list_float: list = []

    for i in range(n):
        list_float.append(wait_random(max_delay))
    result = await asyncio.gather(*list_float)

    list_result: list = []

    for l in result:
            if not list_result:
                list_result.append(l)
                continue

            inserted = False
            for index, element in enumerate(list_result):
                if l < element:
                    list_result.insert(index, l)
                    inserted = True
                    break

            if not inserted:
                list_result.append(l)

    return list_result


