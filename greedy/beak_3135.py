# 준하는 라디오 수집광으로 신제품의 라디오가 나올때마다 흥분을 금치 못한다고 한다.

# 최근 준하가 구입한 라디오는 매우 하이테크 한데, 그 라디오에는 다음과 같은 버튼이 있다.

# 첫 번째 버튼은 주파수를 1MHz 증가시킨다.
# 두 번째 버튼은 주파수를 1MHz 감소시킨다.
# 나머지 N개의 버튼은 즐겨찾기 기능으로, 미리 지정된 주파수로 이동한다.

# 준하는 몸이 안좋아 하루에 손가락을 몇 번 움직이지 못하기 때문에 우리의 도움이 필요하다.
# 현재 주파수 A와 듣고싶은 주파수 B가 주어질 때, 
# 주파수 A에서 B로 갈 때 눌러야 하는 가장 적은 버튼수를 구해주자.

import sys

a, b = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())

typeA = abs(a-b)
bookmarkFreqList = []
for i in range(n):
	bookmarkFreqList.append(int(sys.stdin.readline()))

typeB = 1000
for i in bookmarkFreqList:
	if typeB > abs(b-i):
		typeB = abs(b-i)

if typeA < typeB+1:
	print(typeA)
else:
	print(typeB+1)

# 내장함수 min을 잘 활용하면 코드를 더 줄일 수 있다.