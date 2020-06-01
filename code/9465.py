for T in range(int(input())):
    N = int(input())
    L = [list(map(int, input().split())) for i in range(2)]
    L[0][1], L[1][1] = L[1][0] + L[0][1], L[0][0] + L[1][1]

    for i in range(2, N):
        L[0][i] += max(L[1][i-1], L[1][i-2])
        L[1][i] += max(L[0][i-1], L[0][i-2])

    print(max(L[0][-1], L[1][-1]))
