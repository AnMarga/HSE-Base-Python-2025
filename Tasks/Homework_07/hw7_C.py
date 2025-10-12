import sys

def triangular_numbers(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i
        yield ret

exec(sys.stdin.read())
