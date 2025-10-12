import sys

def factorials(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
        yield ret

exec(sys.stdin.read())
