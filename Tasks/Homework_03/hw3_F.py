a = list(map(int, input().split()))
n = a[0]
a = a[1:]

s = 0

while True:
    i = 0
    flag = False
    new_a = []
    while i < len(a):
        j = i
        while j < len(a) and a[j] == a[i]:
            j += 1
        length = j - i
        if length >= 3:
            s += length
            flag = True
        else:
            new_a.extend(a[i:j])
        i = j
    a = new_a
    if not flag:
        break

print(s)
