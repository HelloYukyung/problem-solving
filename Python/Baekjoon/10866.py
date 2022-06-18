import sys
from collections import deque

input = sys.stdin.readline
deq = deque([])

count = int(input())

for _ in range(count):
    word = input().split()
    order = word[0]
    if order == "push_front":
        deq.appendleft(word[1])
    elif order == "push_back":
        deq.append(word[1])
    elif order == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif order == "pop_back":
        if len(deq) == 0 :
            print(-1)
        else:
            print(deq[-1])
            deq.pop()
    elif order == "size":
        print(len(deq))
    elif order == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif order == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
