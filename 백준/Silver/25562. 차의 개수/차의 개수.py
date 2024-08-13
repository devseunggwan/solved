N = int(input())

print(N * (N - 1) // 2)
print(" ".join([str(2**i) for i in range(N)]))
print(N - 1)
print(" ".join([str(i) for i in range(1, N + 1)]))
