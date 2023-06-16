N, K = map(int, input().strip().split())
M = [False for i in range(N + 1)]
ans = 0
for i in range(2, N + 1):
    if(M[i] == False):
        for j in range(i, N+1, i): 
            if(M[j] == False):
                M[j] = True
                ans += 1
                if(ans == K): 
                    print(j)
                    break