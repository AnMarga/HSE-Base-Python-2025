# не зашло почему-то, PE получил (ошибка представления)

import sys

def babylonian_sequence(a):
    x = 1.0
    while abs(x * x - a) >= 1e-7:
        yield x
        x = 0.5 * (x + a / x)
    yield x

exec(sys.stdin.read())
