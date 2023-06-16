N = int(input())
M = [list(map(int, input().strip().split())) for i in range(N)]
DP = [0 for i in range(N)]

for i in range(N):
    if(i + M[i][0] <= N):
        DP[i] = M[i][1]
        for j in range(i):
            if(j + M[j][0] <= i):
                DP[i] = max(DP[i], DP[j] + M[i][1])
print(max(DP))