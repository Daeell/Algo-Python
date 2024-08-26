N = int(input())
check = [False] * (N+1)
choose = []

def permut(level):
	if level == N:
		print(' '.join(map(str, choose)))
		return

	for i in range(1, N + 1):
		if check[i] == True:
			continue

		choose.append(i)
		check[i] = True

		permut(level + 1)

		check[i] = False
		choose.pop()

permut(0)