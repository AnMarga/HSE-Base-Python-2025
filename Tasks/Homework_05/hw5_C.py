import sys
from typing import Self
from math import sqrt

class Point3D:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Self) -> Self:
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other: Self) -> Self:
        return self.__add__(other)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, other: Self) -> bool:
        return (self.x == other.x and self.y == other.y and self.z == other.z)
    
    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)

    @staticmethod
    def dist(p1: Self, p2: Self) -> float:
        return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)

exec(sys.stdin.read())
