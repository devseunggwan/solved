N, K = map(int, input().strip().split())
Q, R, cnt = 0, 0, 0
L = sorted([list(map(int, input().split()))
            for i in range(N)], key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(len(L)):
    P, cnt = L[i][1] * 1000000000 + L[i][2] * 1000000 + L[i][3], cnt + 1

    if(P != Q):
        Q, R = P, cnt

    if(K == L[i][0]):
        print(R)
        break
