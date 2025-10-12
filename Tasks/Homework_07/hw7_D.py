import sys

def binomial_coefficients(n):
    ret = 1
    yield ret
    for k in range(1, n + 1):
        ret = ret * (n - k + 1) // k
        yield ret

exec(sys.stdin.read())
