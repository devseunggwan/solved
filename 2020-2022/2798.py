N, M = map(int, input().strip().split())
O = list(map(int, input().strip().split()))
ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            num = O[i] + O[k] + O[j]
            if(num > M):
                continue
            else:
                ans = max(ans, num)
print(ans)
