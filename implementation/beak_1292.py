# 백준 1292 구현 문제

# 동호는 내년에 초등학교를 입학한다. 
# 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.
# 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.


import sys

a, b = map(int, sys.stdin.readline().split())

prog_list = []
i = 1
cnt = 1
continueCheck = True
while continueCheck:
	for j in range(1, i+1):
		if cnt > b:
			continueCheck = False
		prog_list.append(i)
		cnt += 1		
	i += 1

total = 0
for i in range(a-1, b):
	total += prog_list[i]

print(total)

# 5줄 정도로 짧게 구현하는 방법 존재. (a,b값은 최대값이 있으므로 수열을 미리 다 저장하고, 파이썬 내장 함수 잘 활용하는 방식)