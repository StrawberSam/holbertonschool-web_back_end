#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.

Returns:
    _type_: float
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Write an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits
    for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns:
        float: numbers
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
