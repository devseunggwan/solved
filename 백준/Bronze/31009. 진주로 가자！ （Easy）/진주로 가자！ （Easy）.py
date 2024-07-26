# https://www.acmicpc.net/problem/31009
import sys


def read_data():
    r = sys.stdin.readline

    N = int(r())
    M = [r().strip().split() for _ in range(N)]
    M = {x[0]: x[1] for x in M}

    return N, M


if __name__ == "__main__":
    N, M = read_data()

    print(M["jinju"])
    print(sum([int(x) > int(M["jinju"]) for x in M.values()]))
