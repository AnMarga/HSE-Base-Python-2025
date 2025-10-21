# don't work

import sys

def make_more(_func=None, *, iters=2):
    try:
        iters = int(iters)
        if iters < 0:
            iters = 1
    except Exception:
        iters = 1

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(iters):
                result = func(*args, **kwargs)
                print(result)
            return result
        return wrapper

    if _func is not None:
        return decorator(_func)

    return decorator

exec(sys.stdin.read())
