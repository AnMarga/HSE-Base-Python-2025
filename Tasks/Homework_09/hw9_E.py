import sys
import time

def limit_timing(func):
    total_time = 0
    def wrapper(*args, **kwargs):
        nonlocal total_time
        start = time.time()
        if total_time > 1:
            return None
        result = func(*args, **kwargs)
        end = time.time()
        total_time += end - start
        if total_time > 1:
            pass
        return result
    return wrapper

exec(sys.stdin.read())
