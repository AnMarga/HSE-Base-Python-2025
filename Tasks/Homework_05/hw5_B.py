import sys
from typing import Self

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int | float) -> Self:
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int | float) -> Self:
        return self.__mul__(scalar)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other: Self) -> bool:
        return (self.x == other.x and self.y == other.y)
    
    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)

    def reverse(self) -> Self:
        return Vector(-self.x, -self.y)

    @staticmethod
    def make_vector(p1: tuple, p2: tuple) -> Self:
        return Vector(x = p2[0] - p1[0], y = p2[1] - p1[1])

exec(sys.stdin.read())
