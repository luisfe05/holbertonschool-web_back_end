#!/usr/bin/env python3
"""Module that collects random numbers with an async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers via an async comprehension over generator."""
    return [i async for i in async_generator()]
