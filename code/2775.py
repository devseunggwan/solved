T = int(input())
for _ in range(T):
    K, N = int(input()), int(input())
    P = [i for i in range(1, N+1)]
    for __ in range(K):
        for j in range(1, N):
            P[j] += P[j-1]
    print(P[-1])
