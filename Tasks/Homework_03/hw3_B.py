a = list(map(int, input().split()))

for i in range(len(a) - 1):
    sgn_left = a[i] >= 0
    sgn_right = a[i + 1] >= 0
    if sgn_left == sgn_right:
        print(a[i], a[i + 1])
        break
