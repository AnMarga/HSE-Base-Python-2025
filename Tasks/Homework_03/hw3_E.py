n, k = map(int, input().split())
a = "I" * n
a = list(a)
for i in range(k):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        a[j] = "."

print("".join(a))
