import sys

# aa
class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int | float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int | float) -> "Vector":
        return self.__mul__(scalar)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

exec(sys.stdin.read())
