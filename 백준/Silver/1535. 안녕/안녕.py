N = int(input())
L = list(map(int, input().split()))
P = list(map(int, input().split()))

# dp[i][j]는 처음부터 i번째까지의 사람을 살펴보고 체력이 j만큼 있을 때 얻을 수 있는 행복의 가치합의 최댓값
dp = [[0 for _ in range(101)] for _ in range(N + 1)]

for i in range(1, N + 1):
    l = L[i - 1]
    p = P[i - 1]

    for j in range(1, 101):
        if l >= j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - l] + p)

print(dp[N][100])