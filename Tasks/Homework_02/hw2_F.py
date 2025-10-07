a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
else:
    if (-b) % a == 0:
        x = -b // a
        if c * x + d != 0:
            print(x)
        else:
            print("NO")
    else:
        print("NO")
