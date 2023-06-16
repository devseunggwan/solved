N = int(input())

DP = [[0 for i in range(1024)] for j in range(10)]
for i in range(1, 10): DP[i][1<<i] = 1

for i in range(1, N):
    DPClone = [[0 for x in range(1024)] for y in range(10)]
    for j in range(0, 10):
        for bit in range(1024):
            if(j != 0): DPClone[j][bit|(1<<j)] = (DPClone[j][bit|(1<<j)] + DP[j-1][bit]) % (10**9)
            if(j != 9): DPClone[j][bit|(1<<j)] = (DPClone[j][bit|(1<<j)] + DP[j+1][bit]) % (10**9)

    DP = DPClone

print(sum([DP[i][1023] for i in range(10)]) % (10**9))
