import sys

n, *arr = map(int, sys.stdin.read().split())
print(*reversed(arr))
