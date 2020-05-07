N, M = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for i in range(N)]
M, K = map(int, input().strip().split())
B = [list(map(int, input().strip().split())) for i in range(M)]

for n in range(N):
    for k in range(K):
        num = 0
        for m in range(M):
            num += A[n][m] * B[m][k]
        print(num, end=" ")
    print()
