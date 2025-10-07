import sys
from typing import Self

class Matrix:
    def __init__(self, data: list[list[int]]) -> None:
        self.m = [row.copy() for row in data]

    def __str__(self) -> str:
        return '\n'.join('\t'.join(str(x) for x in row) for row in self.m)

    def size(self) -> tuple[int, int]:
        return (len(self.m), len(self.m[0]))

    def __add__(self, other: Self) -> Self:
        rows, cols = self.size()
        new_data = [
            [self.m[i][j] + other.m[i][j] for j in range(cols)]
            for i in range(rows)
        ]
        return Matrix(new_data)

    def __mul__(self, scalar: int | float) -> Self:
        rows, cols = self.size()
        new_data = [
            [self.m[i][j] * scalar for j in range(cols)]
            for i in range(rows)
        ]
        return Matrix(new_data)

    __rmul__ = __mul__

exec(sys.stdin.read())
