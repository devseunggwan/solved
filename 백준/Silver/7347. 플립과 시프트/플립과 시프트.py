import sys


def read():
    r = sys.stdin.readline

    T = int(r().strip())
    M = [list(map(int, r().strip().split())) for _ in range(T)]

    return T, M


def agg(M: list[int]):
    N, M = M[0], M[1:]
    sep = {"1": "even", "0": "odd"}
    resp = {"odd_1": 0, "odd_0": 0, "even_1": 0, "even_0": 0}

    for idx, i in enumerate(M):
        resp[f"{sep[str(idx % 2)]}_{i}"] += 1

    return N, resp


if __name__ == "__main__":
    T, M = read()

    for case in M:
        N, resp = agg(case)
        print("YES" if abs(resp["odd_1"] - resp["even_1"]) < 2 or N % 2 == 1 else "NO")
