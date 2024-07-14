#!/usr/bin/env python3
"""a python module to measure the execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_comprehension 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the task
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = time.perf_counter()
    return (end - start)
