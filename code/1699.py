N = int(input())
dp = [0 for i in range(N + 1)]
squares = [i**2 for i in range(1, int(N**0.5) + 1)]
for i in range(1, N + 1):
    tmp = []
    for V in squares:
        if(V > i): break
        else: tmp.append(dp[i - V])
    dp[i] = min(tmp) + 1


print(dp[N])

