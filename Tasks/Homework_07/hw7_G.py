import sys

def binary_sequences(n):
    for i in range(2 ** n):
        yield format(i, f'0{n}b')

exec(sys.stdin.read())
