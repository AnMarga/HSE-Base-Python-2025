import sys

def four(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        s = str(result)
        count = s.count('4')
        for _ in range(count):
            print("ЧЕТЫЫЫЫРЕ")
        return result
    return wrapper

exec(sys.stdin.read())
