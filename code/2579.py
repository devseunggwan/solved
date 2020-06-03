N = int(input())
L = [int(input()) for _ in range(N)]
dp = [L[0], max(L[0]+L[1], L[1]), max(L[0]+L[1], L[1]+L[2])]
for i in range(3, N):
    dp.append(max((dp[i-2] + L[i]), (dp[i-3] + L[i-1] + L[i])))
print(dp[N-1])
