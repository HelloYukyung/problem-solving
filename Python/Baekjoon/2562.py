##refactoring
# 시간 복잡도 :O(n)
import sys 
input= sys.stdin.readline


count = 1
max_n = 0


for i in range(1,10):
    num=int(input())
    if num > max_n:
        max_n = num
        count = i
           
print(max_n)
print(count)


# 시간 복잡도 : O(n^2)

import sys 
input= sys.stdin.readline

num_list = []
count =1
max_n = 0

for i in range(1, 10):
    num_list.append(int(input()))
    
    for num in num_list:
        if num > max_n:
            max_n = num 
            count = i
           
print(max_n)
print(count)


