def comb(index, level):
	global L, C, input_list, choose, vowel, VC, CC
	if level == L:
		if VC <= 0 and CC <=0:
			for c in choose:
				print(c, end="")
			print()
		return
	for i in range(index, C):
		ac = input_list[i]
		if ac in vowel:
			VC -= 1
		else:
			CC -= 1
		choose.append(ac)
		comb(i+1, level+1)
		pc = choose.pop()
		if pc in vowel:
			VC += 1
		else:
			CC += 1

	

L, C = map(int, input().split())
input_list = input().split()
input_list.sort()
choose = []
vowel = ["a", "e", "i", "o", "u"]
VC, CC = 1, 2
comb(0,0)