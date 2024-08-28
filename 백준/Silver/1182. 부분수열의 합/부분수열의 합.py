from itertools import combinations

N, S = map(int, input().split())
lst = list(map(int, input().split()))
result = 0

for i in range(1, N+1):
	for curr in combinations(lst, i):
		if sum(curr) == S:
			result += 1

print(result)