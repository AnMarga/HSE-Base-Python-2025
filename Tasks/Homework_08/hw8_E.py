import sys
from collections import deque

def push_front(dq, num):
    dq.appendleft(num)
    print("ok")

def push_back(dq, num):
    dq.append(num)
    print("ok")

def pop_front(dq):
    print(dq.popleft())

def pop_back(dq):
    print(dq.pop())

def front(dq):
    return dq[0]

def back(dq):
    return dq[-1]

def size(dq):
    return len(dq)

def clear(dq):
    dq.clear()
    return dq

def exit():
    print("bye")

exec(sys.stdin.read())
