N, ans = int(input()), 0
M = sorted([int(input()) for i in range(N)], reverse=True)

for i in range(N):
    if(M[i] - i > 0): ans += M[i] - i
print(ans)