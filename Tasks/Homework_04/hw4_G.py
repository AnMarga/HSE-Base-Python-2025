import sys

def listing_game(n: int, start: int = 1, step: int = 1, direction: int = 1) -> int:
    if n == 1:
        return start
    new_size = n // 2
    if direction == 1:
        new_start = start + step
    else:
        new_start = start if (n % 2 == 0) else (start + step)
    return listing_game(new_size, new_start, step * 2, -direction)

exec(sys.stdin.read())
