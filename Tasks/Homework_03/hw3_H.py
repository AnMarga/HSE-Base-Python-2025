import sys

text = sys.stdin.read().split()
dict = {}
res = []

for word in text:
    res.append(str(dict.get(word, 0)))
    dict[word] = dict.get(word, 0) + 1

print(" ".join(res))
