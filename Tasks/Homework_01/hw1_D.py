n = int(input())
s = 1

if n == 0:
    print(1)
elif n == 1:
    print(2)
else:
    for _ in range(n):
        s *= 2
    print(s)
