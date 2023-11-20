n = int(input())
arr = list(map(str, input().split()))
cnt = 0

for num in arr:
    if int(num[-1]) == n:
        cnt += 1

print(cnt)