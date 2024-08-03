from itertools import combinations_with_replacement


def read():
    N, M = map(int, input().strip().split())
    K = sorted(list(set(map(int, input().strip().split()))))

    return N, M, K


if __name__ == "__main__":
    N, M, K = read()

    resp = list(combinations_with_replacement(K, r=M))
    for item in resp:
        print(" ".join(map(str, item)))
