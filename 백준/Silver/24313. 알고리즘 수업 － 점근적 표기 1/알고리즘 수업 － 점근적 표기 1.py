import sys


def read():
    r = sys.stdin.readline

    a1, a0 = map(int, r().strip().split())
    c = int(r().strip())
    n0 = int(r().strip())

    return a1, a0, c, n0


if __name__ == "__main__":
    a1, a0, c, n0 = read()

    f = lambda n: (a1 * n) + a0
    g = lambda n: n

    print(int((f(n0) <= c * g(n0)) and (a1 <= c)))
