import functools
import time

from util.logger import Logger

""" This decorator woukd Measure Time taken to execute the fucnton """
def measure_time(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        Logger.info(f"{func.__name__} took {time.time() - start:.2f} seconds")
        return result
    return wrapper
    