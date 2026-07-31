# Python - Async

## Description
This project covers asynchronous programming in Python 3 with `asyncio`: `async`/`await` syntax, running coroutines with `asyncio.run`, executing coroutines concurrently with `asyncio.as_completed`, wrapping coroutines in `asyncio.Task` objects, and measuring concurrent runtime. All functions and coroutines are type-annotated for Python 3.8, and every module/function has a real-sentence docstring.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. The basics of async** | `wait_random(max_delay=10)` coroutine that waits a random delay (0 to `max_delay`) and returns it. | `0-basic_async_syntax.py` |
| **1. Let's execute multiple coroutines at the same time with async** | `wait_n(n, max_delay)` spawns `wait_random` `n` times and returns the delays in ascending order without sorting. | `1-concurrent_coroutines.py` |
| **2. Measure the runtime** | `measure_time(n, max_delay)` times `wait_n(n, max_delay)` and returns the average time per call. | `2-measure_runtime.py` |
| **3. Tasks** | `task_wait_random(max_delay)` wraps `wait_random` in an `asyncio.Task` via `asyncio.create_task`. | `3-tasks.py` |
| **4. Tasks** | `task_wait_n(n, max_delay)`, the task-based version of `wait_n`, using `task_wait_random`. | `4-tasks.py` |

## Author
* **Luis Gonzalez** - Holberton School
