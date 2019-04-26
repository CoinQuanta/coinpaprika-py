"""Rate limting decorator used for limiting the amount of HTTP requests sent
per second."""

import time
import functools

def rate_limited(max_per_second):
    min_interval = 1.0 / float(max_per_second)
    def decorator(func):
        last_time_called = [0.0]

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.clock() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            result = func(*args, **kwargs)
            last_time_called[0] = time.clock()
            return result

        return wrapper

    return decorator

#  vim: set ts=4 sw=4 tw=79 ft=python et :
