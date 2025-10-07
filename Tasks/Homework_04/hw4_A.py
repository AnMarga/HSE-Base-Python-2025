import sys

def mul_list(ls: list, v: int):
    for i in range(len(ls)):
        ls[i] *= v

exec(sys.stdin.read())
