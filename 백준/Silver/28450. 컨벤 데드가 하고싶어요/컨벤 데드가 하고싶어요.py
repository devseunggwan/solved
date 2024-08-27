import sys

def read():
    input = sys.stdin.readline

    N, M = map(int, input().strip().split())
    __MAP = [list(map(int, input().strip().split())) for _ in range(N)]
    H = int(input())

    return N, M, __MAP, H


if __name__ == "__main__":
    N, M, __MAP, H = read()

    DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            
            if i - 1 == 0 or j - 1 == 0:
                DP[i][j] = DP[i - 1][j] + DP[i][j - 1] + __MAP[i - 1][j - 1]
            else:
                DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + __MAP[i - 1][j - 1]
    
    if DP[-1][-1] > H:
        print("NO")
    else:
        print("YES")
        print(DP[-1][-1])
