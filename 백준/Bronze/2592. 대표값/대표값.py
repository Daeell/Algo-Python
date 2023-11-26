SUM = 0
MOST = [0 for _ in range(101)]

for _ in range(10):
    n = int(input())
    SUM += n
    MOST[n // 10] += 1

print(SUM // 10)
print(MOST.index(max(MOST)) * 10)