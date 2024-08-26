N = int(input())
check = [False] * (N+1)
choose = []

def permut(level):
	if level == N:
		for c in choose:
			print(c, end=' ')
		print()
		return
	for i in range(1, N+1):
		if check[i] == False:
			choose.append(i)
			check[i] = True
			permut(level+1)
			choose.pop()
			check[i] = False

permut(0)