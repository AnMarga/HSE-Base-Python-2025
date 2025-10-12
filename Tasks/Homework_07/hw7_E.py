import sys

def mod_powers(a, n):
    value = 1
    while True:
        yield value
        value = (value * a) % n
        if value == 1:
            yield value
            break

exec(sys.stdin.read())
