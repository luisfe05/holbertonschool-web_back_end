# Python - Async Comprehension

## Description
This project covers asynchronous generators and async comprehensions in Python 3: writing an `async def` generator that `yield`s values, collecting values from it with a `[x async for x in ...]` comprehension, and running several async comprehensions concurrently with `asyncio.gather` to observe parallel vs. sequential runtime. All coroutines are type-annotated (`typing.AsyncGenerator`, `typing.List`), and every module/function has a real-sentence docstring.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Async Generator** | `async_generator()` coroutine that loops 10 times, waits 1 second each time, and yields a random float between 0 and 10. | `0-async_generator.py` |
| **1. Async Comprehensions** | `async_comprehension()` collects the 10 values from `async_generator` using an async comprehension and returns them. | `1-async_comprehension.py` |
| **2. Run time for four parallel comprehensions** | `measure_runtime()` runs `async_comprehension` four times in parallel via `asyncio.gather` and returns the total runtime (~10s, not ~40s, since the four coroutines' sleeps overlap). | `2-measure_runtime.py` |

## Author
* **Luis Gonzalez** - Holberton School
