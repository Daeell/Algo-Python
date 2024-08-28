N = int(input())

lst = list(tuple(map(int, input().split())) for _ in range(N))
lst = sorted(lst, key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for i in range(3):
	print(lst[i][0], end=' ')