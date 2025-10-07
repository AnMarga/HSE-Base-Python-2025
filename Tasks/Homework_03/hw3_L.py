a = list(map(int, input().split()))
b = list(map(int, input().split()))
count_a = dict()
count_b = dict()

for num in a:
    if num in count_a:
        count_a[num] += 1
    else:
        count_a[num] = 1

for num in b:
    if num in count_b:
        count_b[num] += 1
    else:
        count_b[num] = 1

s = 0
for num in count_a:
    if num in count_b:
        s += min(count_a[num], count_b[num])

print(s)
