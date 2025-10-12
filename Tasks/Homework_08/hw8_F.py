import sys
from collections import deque

def push_front(dq, num):
    dq.appendleft(num)
    print("ok")

def push_back(dq, num):
    dq.append(num)
    print("ok")

def pop_front(dq):
    if dq:
        print(dq.popleft())
    else:
        print("error")

def pop_back(dq):
    if dq:
        print(dq.pop())
    else:
        print("error")

def front(dq):
    if dq:
        return dq[0]
    else:
        return "error"

def back(dq):
    if dq:
        return dq[-1]
    else:
        return "error"

def size(dq):
    return len(dq)

def clear(dq):
    dq.clear()
    return dq

def exit():
    print("bye")

exec(sys.stdin.read())
