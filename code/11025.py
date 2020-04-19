N, K = map(int, input().strip().split())
ans = 0
for i in range(1, N+1):
    ans = (ans+K) % i
print(ans+1)
