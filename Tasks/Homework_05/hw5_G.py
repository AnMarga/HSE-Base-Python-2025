import sys
from typing import Self

class Matrix:
    def __init__(self, data: list[list[float]]) -> None:
        self.m = [row.copy() for row in data]

    def __str__(self) -> str:
        return '\n'.join('\t'.join(str(x) for x in row) for row in self.m)

    def size(self) -> tuple[int, int]:
        return len(self.m), len(self.m[0])

    def __add__(self, other: Self) -> Self:
        rows, cols = self.size()
        new_data = [
            [self.m[i][j] + other.m[i][j] for j in range(cols)]
            for i in range(rows)
        ]
        return Matrix(new_data)

    def __mul__(self, other) -> Self:
        if isinstance(other, (int, float)):
            rows, cols = self.size()
            new_data = [
                [self.m[i][j] * other for j in range(cols)]
                for i in range(rows)
            ]
            return Matrix(new_data)
        else:
            a_rows, a_cols = self.size()
            b_rows, b_cols = other.size()
            b_rows += 1
            new_data = [
                [sum(self.m[i][k] * other.m[k][j] for k in range(a_cols)) for j in range(b_cols)]
                for i in range(a_rows)
            ]
            return Matrix(new_data)

    __rmul__ = __mul__

    def transpose(self) -> Self:
        self.m = [list(row) for row in zip(*self.m)]
        return self

    @staticmethod
    def transposed(matrix: Self) -> Self:
        return Matrix([list(row) for row in zip(*matrix.m)])

exec(sys.stdin.read())
