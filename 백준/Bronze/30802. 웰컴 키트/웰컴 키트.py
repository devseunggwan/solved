def read():
    N = int(input())
    M = list(map(int, input().strip().split()))

    T, P = map(int, input().strip().split())

    return N, M, T, P


if __name__ == "__main__":
    N, M, T, P = read()

    print(sum([x // T + int(x % T > 0) for x in M]))
    print(N // P, N % P)
