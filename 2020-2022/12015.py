from bisect import bisect_left

N = int(input())
A = list(map(int, input().strip().split()))
dp = []

for i in range(N):
    v = bisect_left(dp, A[i])
    if(len(dp) <= v): dp.append(A[i])
    else: dp[v] = A[i]

print(len(dp))
