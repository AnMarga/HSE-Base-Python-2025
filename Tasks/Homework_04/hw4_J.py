import sys

def evaluate(x: int, *args) -> int:
    if not args:
        return 0
    res = 0
    for k in reversed(args):
        res = res * x + k
    return res

exec(sys.stdin.read())
