# 백준 1181 정렬 문제

#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1.길이가 짧은 것부터
# 2.길이가 같으면 사전 순으로

import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
	arr.append(sys.stdin.readline().strip())
arr = set(arr)
arr = [word.lower() for word in arr]
arr.sort()
arr.sort(key = len)

for i in arr:
	print(i)