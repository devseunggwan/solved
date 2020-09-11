N = int(input())
ans = 0
DP = [[0 for i in range(11)] for j in range(101)]
for i in range(1, 10): DP[1][i] = 1;
for i in range(2, N+1):
    for j in range(10):
        if(j == 0): DP[i][0] = DP[i-1][1]%(10**9)
        elif(j == 9): DP[i][9] = DP[i-1][8]%(10**9)
        else: DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1])%(10**9)

for i in range(10): ans += DP[N][i]%(10**9)
print(ans%(10**9))
