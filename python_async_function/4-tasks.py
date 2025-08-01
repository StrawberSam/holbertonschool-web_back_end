#!/usr/bin/env python3
"""
Module that defines an async routine to run multiple task_wait_random
calls concurrently and return their results in ascending order.

Returns:
    _type_: list of float
"""
import asyncio
import typing


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Run task_wait_random n times concurrently and return sorted results.

    This async function spawns n asyncio tasks using task_wait_random with
    the given max_delay, runs them concurrently, and returns a sorted list
    of the resulting delays.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task in seconds.

    Returns:
        List[float]: Sorted list of delays returned by the tasks.
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    list_float: list = []

    for i in range(n):
        list_float.append(task_wait_random(max_delay))
    result = await asyncio.gather(*list_float)

    return sorted(result)
