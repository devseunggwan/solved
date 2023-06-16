A, B, N = map(int, input().strip().split())
A %= B
for i in range(N-1):
    A *= 10
    A %= B
A *= 10
print(int(A/B))
