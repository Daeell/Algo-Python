N = int(input())
cnt = 0

for i in range(1, N + 1):
    sn = str(i)
    if len(sn) <= 1:
        cnt += 1
    else:
        ivt = int(sn[1]) - int(sn[0])
        if all(int(sn[j]) - int(sn[j - 1]) == ivt for j in range(2, len(sn))):
            cnt += 1

print(cnt)