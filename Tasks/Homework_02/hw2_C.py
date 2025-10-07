a = int(input())
b = int(input())
c = int(input())

even = False
odd = False

if ((a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0)):
    even = True
if ((a % 2 != 0) or (b % 2 != 0) or (c % 2 != 0)):
    odd = True

if (even and odd):
    print("YES")
else:
    print("NO")
