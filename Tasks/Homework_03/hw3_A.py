s = input()
k = 0
ind = 0

for symb in s:
    if symb == 'f':
        k += 1
    ind += 1
    if k == 2:
        print(ind - 1)
        break

if k == 1:
    print(-1)
if k == 0:
    print(-2)
