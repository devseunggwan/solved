if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    T = map(int, input().strip().split())
    T = sorted(T)

    answer = T[-1]

    for i in range(1, K):
        if i % 2 == 0:
            answer += T[-((i // 2) + 1)] - T[(i // 2) - 1]

    print(answer)
