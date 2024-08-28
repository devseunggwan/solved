import sys
from collections import Counter


def read():
    input = sys.stdin.readline

    N = int(input().strip())
    M = [(Counter(input().strip().split()[1:]), Counter(input().strip().split()[1:])) for _ in range(N)]

    return N, M


def think(A, B) -> str:
    for i in map(str, range(4, 0, -1)):
        if A[i] != B[i]:            
            return "A" if A[i] > B[i] else "B"

    return "D"


if __name__ == "__main__":
    N, M = read()

    for A, B in M:
        print(think(A, B))
