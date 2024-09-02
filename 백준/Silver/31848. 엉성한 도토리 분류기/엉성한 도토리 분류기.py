import bisect


def read():
    N = int(input())
    A = [
        (idx + 1, x + idx)
        for idx, x in enumerate(list(map(int, input().strip().split())))
    ]
    Q = int(input())
    S = list(map(int, input().strip().split()))

    return N, A, Q, S


def filter(A) -> list[tuple[int, int]]:
    bef = -1
    new_idx = []
    new_a = []

    for idx, i in A:
        if i > bef:
            new_idx.append(idx)
            new_a.append(i)
            bef = i

    return new_idx, new_a


if __name__ == "__main__":
    N, A, Q, S = read()

    IDX, A = filter(A)

    print(" ".join(map(str, [IDX[bisect.bisect_left(A, i)] for i in S])))
