import sys


def read():
    input = sys.stdin.readline

    N = int(input())
    DP = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N-1):
        _, C = int(input()), map(int, input().strip().split())

        for j in C:
            DP[i][j-1] = 1

    return N, DP


def floyd_warshall(N, DP):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if DP[i][k] and DP[k][j]:
                    DP[i][j] = 1

    return DP


def is_cycle(N, DP):
    for i in range(N):
        if DP[i][i] and DP[0][i]:
            return True

    return False

if __name__ == "__main__":
    N, DP = read()
    DP = floyd_warshall(N, DP)    
    print("CYCLE" if is_cycle(N, DP) else "NO CYCLE")
