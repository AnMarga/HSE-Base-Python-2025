n = int(input())
d = dict()

for _ in range(n):
    a, b = input().split()
    d[a] = b
    d[b] = a
search = input()

print(d[search])
