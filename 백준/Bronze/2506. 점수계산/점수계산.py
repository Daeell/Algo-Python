n = int(input())
numbers = list(map(int, input().split()))
cnt = 0
tmp = 0

for num in numbers:
    if num:
        tmp += 1
    else:
        tmp = 0
    cnt += tmp

print(cnt)