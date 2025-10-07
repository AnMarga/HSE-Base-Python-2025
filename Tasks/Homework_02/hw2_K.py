num = int(input())
m1 = -1
m2 = -2

while num != 0:
    if num >= m1:
        m2 = m1
        m1 = num
    else:
        if num > m2:
            m2 = num
    num = int(input())

print(m2)
