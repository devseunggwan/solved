N, M = map(int, input().strip().split())
L = [list(map(int, input().strip().split())) for i in range(N)]
dp = [[0 for i in range(M)] for j in range(N)] 

for q in range(N):
    for p in range(M):
        if(p == 0):
            dp[q][p] = L[q][p]
        else:
            dp[q][p] = dp[q][p-1] + L[q][p]
print(dp)

for T in range(int(input())):
    i, j, x, y = map(int, input().strip().split())

    print(sum())