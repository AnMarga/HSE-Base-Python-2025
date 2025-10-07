a = int(input())
b = int(input())
c = int(input())

if ((a + b > c) and (b + c > a) and (a + c > b)):
    if ((a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2)):
        print("right")
    elif ((a**2 + b**2 < c**2) or (b**2 + c**2 < a**2) or (a**2 + c**2 < b**2)):
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")
