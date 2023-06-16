n, r = map(int, input().split())
N, R, NR = 1, 1, 1

for i in range(1, n+1):
    N *= i
for i in range(1, r + 1):
    R *= i
for i in range(1, n-r+1):
    NR *= i

print(N//(R*NR))
