import sys

text = sys.stdin.read().split()
d = dict()

for word in text:
    d[word] = d.get(word, 0) + 1

m = max(d.values())
v = [word for word, count in d.items() if count == m]
print(min(v))
