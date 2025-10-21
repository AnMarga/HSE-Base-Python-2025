import sys
from functools import wraps

def where_am_i(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} with arguments {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

exec(sys.stdin.read())
