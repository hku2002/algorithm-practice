# 백준 2960 구현

# 실패하여 다시 풀이 필요

import sys

n, k = map(int, sys.stdin.readline().split())
arr = [True] * (n-1)
cnt = 0

for i in (2, n+1):
	for j in range(i, i+1, i):
		if arr[j]:
			arr[j] = false
			cnt += 1
			if cnt == k:
				print(j)
				break
