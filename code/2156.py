N = int(input())
M = [int(input()) for i in range(N)]
dp = [0 for i in range(N + 1)]
if(N == 1): dp[1] = M[0]
else: dp[1], dp[2] = M[0], M[0] + M[1]

for i in range(3, N+1):
    dp[i] = max(M[i-1] + dp[i-2], M[i-1] + M[i-2] + dp[i-3], dp[i-1])

print(dp[-1])