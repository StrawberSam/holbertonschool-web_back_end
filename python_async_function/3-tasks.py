#!/usr/bin/env python3
"""
Module that provides a synchronous function to create asyncio Tasks
for running the wait_random coroutine asynchronously.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task that runs wait_random with the
    given max_delay.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: The task object that wraps the execution of wait_random.
    """
    # créer une Task à partir de wait_random(max_delay)
    task = asyncio.create_task(wait_random(max_delay))
    # la retourner
    return task
