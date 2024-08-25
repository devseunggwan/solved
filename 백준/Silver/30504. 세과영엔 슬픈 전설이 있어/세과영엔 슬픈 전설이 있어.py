import sys


def read():
    r = sys.stdin.readline
    N = int(r())

    A = sorted(list(enumerate(map(int, r().strip().split()))), key=lambda x: x[1])
    B = sorted(list(map(int, r().strip().split())))

    return N, A, B


if __name__ == "__main__":
    N, A, B = read()
    answer = [None] * N
    idx = 0

    for origin_idx, num in A:
        while idx < N and B[idx] < num:
            idx += 1

        if idx < N:
            answer[origin_idx] = B[idx]
            idx += 1
        else:
            answer = "-1"
            break

    print(" ".join(map(str, answer)) if isinstance(answer, list) else -1)
