R = 6
choose = []

def combination(index, level):
	if level == R:
		for i in choose:
			print(i, end=" ")
		print()
		return
	for i in range(index, k+1):
		choose.append(input_list[i])
		combination(i+1, level+1)
		choose.pop()

while True:
	input_list = list(map(int, input().split()))
	k = input_list[0]
	if k == 0:
		break
	combination(1, 0)
	print()