from itertools import permutations

word = input()
res = 0

def fact(x):
	if x == 0:
		return 1
	return x * fact(x-1) 

for curr in permutations(word):
	ok = True
	for i in range(len(curr)-1):
		if curr[i] == curr[i+1]:
			ok = False
			break
	if ok:
		res += 1

for i in range(ord('a'), ord('z')+1):
	res //= fact(word.count(chr(i)))

print(res)