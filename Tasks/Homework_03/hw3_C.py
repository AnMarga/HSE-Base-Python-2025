a = list(map(int, input().split()))
h = int(input())

k = 1
for val in a:
    if val >= h:
        k += 1
    else:
        break

print(k)
