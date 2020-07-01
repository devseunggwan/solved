N = int(input())
M = list(map(int, input().strip().split()))
dp = [0 for i in range(N)]


for i in range(N):
    if(N%(i+1) == 0):
        dp[i] = (M[i]*N)//(i+1)
    else:
        dp[i] = (M[i]*N)//(i+1) + M[N%i-1]

print(dp)