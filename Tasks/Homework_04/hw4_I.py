import sys

def matching(s: str, p: str) -> bool:
    if not p:
        return not s

    match = bool(s) and (p[0] == s[0] or p[0] == '.')

    if len(p) >= 2 and p[1] == '*':
        return (matching(s, p[2:]) or
                (match and matching(s[1:], p)))
    else:
        return match and matching(s[1:], p[1:])

exec(sys.stdin.read())
