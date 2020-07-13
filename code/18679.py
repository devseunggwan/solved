D, M = dict(), int(input())
for _ in range(M):
    X, Y = input().strip().split(" = ")
    D[X] = Y

for _ in range(int(input())):
    N = int(input())
    S = input().strip().split()

    for i in range(len(S)):
        S[i] = D[S[i]]
    print(*S)