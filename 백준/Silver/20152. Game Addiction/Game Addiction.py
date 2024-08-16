H, N = map(int, input().strip().split())

square = abs(H - N) + 1

DP = [[0 for _ in range(square)] for _ in range(square)]

for i in range(square):
    DP[0][i] = 1

for i in range(1, square):
    for j in range(i, square):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1]

print(DP[-1][-1])
