# wtf

import sys

def generate_sequences(n, k):
    for i in range(k ** n):
        yield format(i, f'0{n}').replace(' ', '').rjust(n, '0') if k == 10 else to_base_k(i, k, n)

def to_base_k(num, base, length):
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    digits = digits[::-1]
    while len(digits) < length:
        digits.insert(0, '0')
    return ''.join(digits)

exec(sys.stdin.read())
