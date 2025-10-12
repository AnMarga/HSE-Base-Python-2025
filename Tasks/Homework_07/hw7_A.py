import sys

def square_fibonacci(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a * a
        a, b = b, a + b

exec(sys.stdin.read())
