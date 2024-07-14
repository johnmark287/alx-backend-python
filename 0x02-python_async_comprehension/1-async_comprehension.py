#!/usr/bin/env python3
"""A coroutine that lcollect 10 random numbers
using an async comprehensing over async_generator"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing
    over async_generator and return 10 randon numbers
    """
    return [n async for n in async_generator()]
