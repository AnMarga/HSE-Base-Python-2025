import sys

def change_register(s: str) -> str:
    res = []
    for i in range(len(s)):
        if s[i].isupper() and i > 0:
            res.append('_')
        res.append(s[i].lower())
    return ''.join(res)

exec(sys.stdin.read())
