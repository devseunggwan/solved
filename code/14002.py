from collections import deque

N = int(input())
A = list(map(int, input().strip().split()))
dp = [0 for i in range(N)]
ans = deque()

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if(A[i] > A[j]): 
            dp[i] = max(dp[i], dp[j]+1)

V = max(dp)
for i in range(N-1, -1, -1):
    if(dp[i] == V):
        ans.appendleft(A[i])
        V -= 1

print(max(dp))
print(*(list(ans)))