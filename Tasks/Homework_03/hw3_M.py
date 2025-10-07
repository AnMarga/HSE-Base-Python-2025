n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for x in a:
    for i in range(len(b)):
        if b[i] == x:
            print(x, end=' ')
            b[i] = None
            break
