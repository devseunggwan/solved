import sys

for T in range(int(input())):
    N = int(input())
    G = sorted([list(map(int, sys.stdin.readline().strip().split())) for g in range(N)], key=lambda x: x[0])
    ans, tmp = 1, G[0][1]

    for i in range(1, N):
        if(G[i][1] < tmp):
            ans += 1
            tmp = G[i][1]

    print(ans)
