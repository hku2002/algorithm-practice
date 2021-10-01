# 백준 7568 구현 문제

import sys

n = int(sys.stdin.readline().strip())
sizeList = []

for i in range(n):
	sizeList.append(list(map(int, sys.stdin.readline().split())))

gradeList = []
tempList = []
cnt = 0
for i in range(n):
	for j in range(n):
		if sizeList[i][0] < sizeList[j][0]:
			tempList.append(sizeList[j][1])

	for a in tempList:
		if sizeList[i][1] < a:
			cnt +=  1
	tempList.clear()
	print(cnt+1, end=' ')
	gradeList.append(cnt+1)
	cnt = 0

# if 문을 잘 쓰면 조금 더 효율적인 코드가 됨