import math

def IsPrime(n: int) -> bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

n = int(input())

print("YES" if IsPrime(n) else "NO")
