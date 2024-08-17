import sys


def read():
    input = sys.stdin.readline

    R, Q = map(int, input().strip().split())
    N = list(map(int, input().strip().split()))
    QUERY = [list(map(int, input().strip().split())) for _ in range(Q)]

    return R, Q, N, QUERY


def continous_sum(N):
    T = 0
    CS = [0]

    for i in N:
        T += i
        CS.append(T)

    return CS


if __name__ == "__main__":
    R, Q, N, QUERY = read()
    CS = continous_sum(N)
    idx = 0

    for x in QUERY:
        if x[0] == 3:
            a = (x[1] - 1 + idx) % R
            b = (x[2] - 1 + idx) % R

            print(CS[b + 1] - CS[a] + (0 if a <= b else CS[R]))

        else:
            idx = (idx + (x[1] if x[0] == 2 else -x[1]) + R) % R
