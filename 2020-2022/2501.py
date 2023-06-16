N, K = map(int, input().strip().split())
try:
    ans = ["_"]
    for i in range(1, N+1):
        if(N % i == 0):
            ans.append(i)

    print(ans[K])

except:
    print(0)
