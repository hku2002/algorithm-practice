# 백준 11656 문자열 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

from string import ascii_lowercase
import sys

s = sys.stdin.readline().strip()
alphaList = list(ascii_lowercase)

resultList = []
for i in range(len(alphaList)):
	cnt = 0
	for j in s:
		if alphaList[i] == j:
			cnt += 1
	resultList.append(cnt)
	print(cnt, end=' ')

# 아스키 코드 변환을 잘 활용한 시간복잡도 O(2n)이 나오는 방식 존재(현재는 O(n*2)임)