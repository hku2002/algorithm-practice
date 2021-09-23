# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
	arr.append(list(map(int, sys.stdin.readline().split())))
	
arr.sort()
for i in arr:
	result = str(i)
	result = result.replace('[', '')
	result = result.replace(']', '')
	result = result.replace(',', '')
	print(result)

# 11줄 for문 하단 5줄은
# print(i[0], i[1]) 1줄로 표현이 가능하다... ^^;