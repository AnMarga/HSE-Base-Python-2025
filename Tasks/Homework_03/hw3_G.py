a = [tuple(map(int, input().split())) for _ in range(8)]

flag = False
for i in range(8):
    for j in range(i + 1, 8):
        x1, y1 = a[i]
        x2, y2 = a[j]
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            flag = True
            break
    if flag:
        break

if flag:
    print("YES")
else:
    print("NO")
