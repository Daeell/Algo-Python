from itertools import combinations

vowels = ['a','e','i','o','u']

def is_possible(word):
	global L
	vow = 0
	for c in word:
		vow += (c in vowels)
	con = L - vow

	return (vow >= 1 and con >= 2)

L, C = map(int, input().split())
arr = input().split()
arr.sort()

for word in combinations(arr,L):
	if is_possible(word):
		print(''.join(word))