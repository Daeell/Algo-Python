arr = [" " for _ in range(13)]
arr[0] = "-"

for i in range(1, 13):
	arr[i] = arr[i-1] + " " * (3 ** (i-1)) + arr[i-1]

while True:
	try:
		n = int(input())
		print(arr[n])
	except:
		break