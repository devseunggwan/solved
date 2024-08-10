import sys


def read():
    r = sys.stdin.readline

    N, M = map(int, r().strip().split())
    A = [0] + list(map(int, r().strip().split()))
    C = [0] + list(map(int, r().strip().split()))

    DP = [[0 for _ in range(sum(C) + 1)] for _ in range(N + 1)]

    return N, M, A, C, DP


if __name__ == "__main__":
    N, M, A, C, DP = read()

    answer = sum(C)

    for i in range(1, N + 1):
        for j in range(sum(C) + 1):
            DP[i][j] = (
                DP[i - 1][j]
                if j < C[i]
                else max(DP[i - 1][j], DP[i - 1][j - C[i]] + A[i])
            )

            if DP[i][j] >= M:
                answer = min(answer, j)

    print(answer)
