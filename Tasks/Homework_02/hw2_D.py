a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b // c >= 2:
        if a // b <= 2:
            print("good")
        else:
            print("bad")
    else:
        print("bad")
else:
    if a // c >= 2:
        if b // a <= 2:
            print("good")
        else:
            print("bad")
    else:
        print("bad")
