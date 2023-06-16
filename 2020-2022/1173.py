N, m, M, T, R = map(int, input().strip().split())
t, A, X = 0, -1, m

if(m + T > M):
    print(-1)
else:
    while t != N:
        A += 1
        if(X + T < M):
            X += T
            t += 1
        else:
            if(X-R < m):
                X = m
            else:
                X -= R

    print(A)
