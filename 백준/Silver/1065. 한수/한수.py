N = int(input())
cnt = 0

for i in range(1, N + 1):
    n = str(i)
    if len(n) == 1 or len(n) == 2:
        cnt += 1
    else:
        itv = int(n[1]) - int(n[0])
        flag = True
        for j in range(2, len(n)):
            tmp = int(n[j]) - int(n[j - 1])
            if itv != tmp:
                flag = False
                break
        if flag == True:
            cnt += 1

print(cnt)
