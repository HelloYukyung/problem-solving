import sys 
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    zero = [1,0,1]
    one = [0,1,1]
    if N >= 3:
        for i in range(3, N+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[N], one[N])