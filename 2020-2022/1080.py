def func():
    N, M = map(int, input().split())

    A = [list(map(int,list(input()))) for i in range(N)]
    B = [list(map(int,list(input()))) for i in range(N)]
    G = [[True for i in range(M)] for j in range(N)]

    for i in range(N):
        for j in range(M):
            if(A[i][j] ^ B[i][j]):
                G[i][j] = False
    ans = 0

    for i in range(N-2):
        for j in range(M-2):
            if(G[i][j] == False):
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        G[x][y] = not G[x][y]
                ans += 1

                if(False not in G):
                    return ans

        if(G[i][M-1] == False):
            return -1


print(func())
