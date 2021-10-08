# 백준 9237 그리디 알고리즘 문제

# 농부 상근이는 마당에 심기 위한 나무 묘목 n개를 구입했다. 
# 묘목 하나를 심는데 걸리는 시간은 1일이고, 상근이는 각 묘목이 다 자라는데 며칠이 걸리는지 정확하게 알고 있다.
# 상근이는 마을 이장님을 초대해 자신이 심은 나무를 자랑하려고 한다. 
# 이장님을 실망시키면 안되기 때문에, 모든 나무가 완전히 자란 이후에 이장님을 초대하려고 한다. 
# 즉, 마지막 나무가 다 자란 다음날 이장님을 초대할 것이다.
# 상근이는 나무를 심는 순서를 신중하게 골라 이장님을 최대한 빨리 초대하려고 한다. 
# 이장님을 며칠에 초대할 수 있을까?

import sys

n = int(sys.stdin.readline())
timeList = list(map(int, sys.stdin.readline().split()))
timeList.sort(reverse = True)

maxTime, plantingTime= 0, 0
for i in range(len(timeList)):
	if (timeList[i] + i + 1) > maxTime:
		maxTime = timeList[i] + i + 1

print(maxTime+1)