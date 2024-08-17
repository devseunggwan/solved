N, M = map(int, input().strip().split())

print(min(N, M) * 2 - 1 - int(N <= M))
