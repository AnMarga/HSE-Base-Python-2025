a = list(map(int, input().split()))
k = 0

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            k += 1

print(k)
