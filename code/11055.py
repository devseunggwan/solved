N = int(input())
A = list(map(int, input().strip().split()))
dp = [0 for i in range(N)]
ans = 0

for i in range(N):
    dp[i] = A[i]
    for j in range(i):
        if(A[i] > A[j]): 
            dp[i] = max(dp[i], dp[j]+A[i])
    ans = max(ans, dp[i])

print(ans)