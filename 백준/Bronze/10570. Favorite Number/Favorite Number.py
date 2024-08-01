import sys
from collections import Counter


def read():
    r = sys.stdin.readline

    T = int(r().strip())
    data = []

    for _ in range(T):
        V = int(r().strip())
        S = list(Counter([int(r().strip()) for _ in range(V)]).items())
        max_count = max([x[1] for x in S])

        S = min([x[0] for x in S if x[1] == max_count])

        data.append((V, S))

    return T, data


if __name__ == "__main__":
    T, testcases = read()

    for V, S in testcases:
        print(S)
