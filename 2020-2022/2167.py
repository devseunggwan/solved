N, M = map(int, input().strip().split())
L = [list(map(int, input().strip().split())) for i in range(N)]
dp = [[0 for i in range(M + 1)] for j in range(N + 1)]

for q in range(1, N + 1):
    for p in range(1, M + 1):
        dp[q][p] = L[q-1][p-1] + dp[q-1][p] + dp[q][p-1] - dp[q-1][p-1]

for T in range(int(input())):
    i, j, x, y = map(int, input().strip().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
