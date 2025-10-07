import math

def ReduceFraction(n: int, m: int):
    g = math.gcd(n, m)
    return (n // g, m // g)

n = int(input())
m = int(input())

a, b = ReduceFraction(n, m)
print(a, b)
