N, K = map(int, input().strip().split())
M = [i for i in range(1, N+1)]
ans = []
tmp = K - 1

for i in range(N):
    if(len(M) <= tmp):
        tmp %= len(M)

    ans.append(M.pop(tmp))
    tmp += K-1

print("<", end="")
for i in range(N):
    if(i == N-1):
        print(str(ans[i])+">", end="")
    else:
        print(str(ans[i]) + ",", end=" ")
