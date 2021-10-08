# 백준 5555 문자열 문제

# 당신은 N개의 반지를 가지고 있다. 
# 각각의 반지는 대문자 10 문자로 이루어진 문자열이 새겨져 있다. 
# 반지는 문자열의 시작과 끝이 연결된 형태로 문자가 새겨져 있다. 
# 반지에 각인된 문자열을 거꾸로 읽는 걱정은 없다.
# 찾고자하는 문자열이 주어졌을 때 그 문자열을 포함하는 반지가 몇 개인지를 발견하는 프로그램을 작성하라.


import sys

s = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
total = 0
for i in range(n):
	a = sys.stdin.readline().strip()
	for j in range(len(s)-1):
		a += a[j]
	if s in a:
		total += 1

print(total)


# 두 번째 for문 대신 그냥 전체를 덧붙이면(a += a) for문이 필요 없음