import asyncio
import concurrent.futures
from time import sleep


def invoke(func, payload):
    print(f'Invoking function with payload {payload}')
    sleep(1)  # Simulate a time-consuming task
    return func(*payload)


async def run(func, data, n_workers=4):
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(executor, invoke, func, payload) for payload in data]
        responses = await asyncio.gather(*tasks)
    return responses


def parallelize(func, data, n_workers=4):
    print(f'Parallelizing with {n_workers} workers')
    return asyncio.run(run(func, data, n_workers=n_workers))


__all__ = ['parallelize']
