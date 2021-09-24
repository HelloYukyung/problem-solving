## 수 정렬하기 2 
# ====문제 
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오 

# ====입력 
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

#----풀이 
# -입력되는 수는 중복되지 않는다. -> python 내장함수 set 사용
# -입력된 수를 오름차순으로 정렬한 결과를 출력한다. -> sort 사용

## sorted함수 이용  pypy3

n= int(input())
num =[]

for _ in range(n):
    x= int(input())
    num.append(x)

for i in sorted(num):
    print(i)


