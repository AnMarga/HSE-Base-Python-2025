import sys
from itertools import accumulate

words = sys.stdin.read().split()
for line in accumulate(words, lambda a, b: a + ' ' + b):
    print(line)
