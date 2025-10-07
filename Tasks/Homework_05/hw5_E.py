import sys
from typing import Self

class Matrix:
    def __init__(self, data: list[list[int]]) -> None:
        self.m = [row.copy() for row in data]

    def __str__(self) -> str:
        return '\n'.join('\t'.join(str(x) for x in row) for row in self.m)

    def size(self) -> tuple[int, int]:
        return (len(self.m), len(self.m[0]))

exec(sys.stdin.read())
