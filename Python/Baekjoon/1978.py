import sys 
input =sys.stdin.readline

n = int(input())
sosu = list(map(int, input().split()))

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            print(num,i)
            return False
    return True

    
count = 0

for i in sosu:
    if prime(i):
        count += 1
print(count)