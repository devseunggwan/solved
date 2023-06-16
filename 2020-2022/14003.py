from bisect import bisect_left
from collections import deque

N = int(input())
A = list(map(int, input().strip().split()))
dp, M, ans = [], [0 for i in range(N)], deque()

for i in range(N):
    v = bisect_left(dp, A[i])
    if(len(dp) <= v): dp.append(A[i])
    else: dp[v] = A[i]
    M[i] = v
    
print(M)
W = len(dp)

for i in range(N-1, -1, -1):
    if(W == M[i]):
        ans.appendleft(A[i])
        W -= 1

print(len(dp))
print(*(list(ans)))