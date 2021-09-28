# 백준 1966 구현 문제

import sys

testCase = int(sys.stdin.readline().strip())
for i in range(testCase):

	a, b = map(int, sys.stdin.readline().split())
	queueList = list(map(int, sys.stdin.readline().split()))
	checkList = [0 for _ in range(a)]
	checkList[b] = 'check'
	cnt = 0
	while True:
		if queueList[0] == max(queueList):
			cnt += 1

			if checkList[0] == 'check':
				print(cnt)
				break
			else:
				del queueList[0]
				del checkList[0]
		else:
			queueList.append(queueList[0])
			checkList.append(checkList[0])
			del queueList[0]
			del checkList[0]

# 실패하여 해답 확인 후 커밋