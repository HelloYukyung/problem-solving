# ====덱

# ----문제 
# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# ----입력 
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# ---- 출력 

# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# #----풀이 
# deque 라이브러리를 사용하여 문제 풀기 
# Deque(데크): double-ended queue 의 줄임말로, 앞과 뒤에서 즉, 양방향에서 데이터를 처리할 수 있는 queue형 자료구조

import sys
from collections import deque

input= sys.stdin.readline

N= int(input()) # 명령의 수 

dq =deque()

for _ in range(N):
    Order = list(input().split())

    if Order[0] =="push_front":
        dq.appendleft(Order[1]) 
    elif Order[0] == "push_back":
        dq.append(Order[1])
    
    elif Order[0] =="pop_front":
        if len(dq) == 0:
            print(-1)
        else :
            print(dq.popleft())

    elif Order[0] =="pop_back":
        if len(dq)==0:
            print(-1)
        else:
            print(dq.pop())
    elif Order[0] =="size":
        print(len(dq))
    
    elif Order[0]=="empty":
        if len(dq) == 0:
            print(1)
        else :
            print(0)

    elif Order[0]=="front":
        if len(dq)==0:
            print(-1)
        else :
            print(dq[0])
        
    elif Order[0]=="back":
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])