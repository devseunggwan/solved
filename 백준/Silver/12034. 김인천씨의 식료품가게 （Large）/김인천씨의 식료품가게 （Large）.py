import sys


def read():
    input = sys.stdin.readline

    T = int(input())
    M = [(int(input()), list(map(int, input().strip().split()))) for _ in range(T)]

    return M


if __name__ == "__main__":
    M = read()

    for idx, case in enumerate(M):
        answer = []
        N, C = case
        __is_find = [1 for _ in range(N * 2)]

        for i in range(N * 2):
            if __is_find[i]:
                answer.append(str(C[i]))
                __is_find[i] == 0
                __find = int(C[i] * 4 / 3)

                for j in range(i, N * 2):
                    if __find == C[j] and __is_find[j]:
                        __is_find[j] = 0
                        break
        
        print(f"Case #{idx + 1}: " + " ".join(answer))
