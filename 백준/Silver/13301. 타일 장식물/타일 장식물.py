def factorial(N):
    A, B = 1, 0

    for _ in range(1, N):
        A, B = A + B, A

    return A, B


if __name__ == "__main__":
    N = int(input())
    A, B = factorial(N)

    print(4 * A + 2 * B)
