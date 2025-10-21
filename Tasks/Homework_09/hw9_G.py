import sys
import time
from functools import wraps

_total_time = {}
_no_limit_funcs = []

def destroy_limitation(func):
    if len(_no_limit_funcs) < 3 and func not in _no_limit_funcs:
        _no_limit_funcs.append(func)
        func.no_limitation = 1
    return func

def limit_timing(func):
    total_time = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total_time

        if getattr(func, 'no_limitation', 0) == 1:
            return func(*args, **kwargs)

        if total_time > 1:
            return None

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        total_time += end - start
        return result

    return wrapper

exec(sys.stdin.read())
