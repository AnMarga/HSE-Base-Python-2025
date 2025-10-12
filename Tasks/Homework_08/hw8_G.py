import sys
import re
from collections import Counter

def find_most_common_words(text, num):
    words = re.findall(r'[A-Za-zА-Яа-я]+', text)
    counter = Counter(words)
    return counter.most_common(num)

exec(sys.stdin.read())
