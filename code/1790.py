N, K = map(int, input().split())

L = [9, 90 * 2, 900 * 3, 9000 * 4, 90000 * 5, 900000 * 6, 9000000 * 7, 90000000 * 8]
if(N < 10):
    if(N < K):
        print(-1)
    else:
        print(N - K + 1)

else:
    A, B = sum(L[:len(str(N))-1]), (len(str(N)) * (N - (10 ** (len(str(N))-1)) + 1))
    if(A + B < K): print(-1)
    else:
        sums, idx = 0, 0
        for i in L:
            if(sums + i < A + B - K):
                sums += i
                idx += 1
            else:
                break

        x, y = (A + B - K - sums)//(idx + 1), (A + B - K - sums)%(idx + 1)
        print(x, y, sums, idx)