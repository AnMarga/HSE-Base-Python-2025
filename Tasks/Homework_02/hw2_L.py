a = int(input())

f1 = 0
f2 = 1
n = 0

while f1 < a:
    f1, f2 = f2, f1 + f2
    n += 1

if f1 == a:
    print(n)
else:
    print(-1)
