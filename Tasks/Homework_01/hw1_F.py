a = int(input())
b = int(input())
n = int(input())

a_sum = a * n
b_sum = b * n
a_sum += b_sum // 100
b_sum %= 100

print(a_sum, b_sum)
