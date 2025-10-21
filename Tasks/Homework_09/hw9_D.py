import sys

def have_good_values(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, (int, float)):
                arg = abs(int(arg))
            elif isinstance(arg, str):
                arg = arg.strip().lower()
            new_args.append(arg)
        return func(*new_args, **kwargs)
    return wrapper

exec(sys.stdin.read())
