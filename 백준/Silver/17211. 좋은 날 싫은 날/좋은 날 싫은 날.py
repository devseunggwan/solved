import sys


def read():
    r = sys.stdin.readline
    N, F = map(int, r().strip().split())
    M = list(map(float, r().strip().split()))
    F = [int(F == 0), int(F == 1)]

    return N, M, F


if __name__ == "__main__":
    N, M, F = read()

    for _ in range(N):
        F = [F[0] * M[0] + F[1] * M[2], F[0] * M[1] + F[1] * M[3]]

    for i in F:
        print(int(i * 1000))
