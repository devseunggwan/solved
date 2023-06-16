N = int(input())
M = list(map(int, input().strip().split()))
dp = [M[0]]
for i in range(N-1):
    dp.append(max(dp[i]+M[i+1], M[i+1]))

print(max(dp))