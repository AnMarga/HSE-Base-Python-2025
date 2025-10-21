import sys

def beautiful_output(symbol='-'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            line = (symbol * ((30 + len(symbol) - 1) // len(symbol)))[:30]
            print(line)
            func(*args, **kwargs)
            print(line)
        return wrapper
    return decorator

exec(sys.stdin.read())
