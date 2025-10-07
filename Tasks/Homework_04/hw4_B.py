import sys

def check(a: list, b: list) -> int: 
    return 1 if set(a) == set(b) else 0

exec(sys.stdin.read())
