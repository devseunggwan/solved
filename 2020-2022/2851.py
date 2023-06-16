M = [int(input()) for i in range(10)]
N = [sum(M[:i]) for i in range(1, 11)]
K = [abs(sum(M[:i]) - 100) for i in range(1, 11)]
ans, tmp = 0, 100
for k in range(9, -1, -1):
    if(K[k] < tmp):
        tmp = K[k]
        ans = k

print(N[ans])
