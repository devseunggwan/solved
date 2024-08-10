N = int(input())
print(sum([((N - i - 2) // 2) for i in range(2, N - 1, 2)]))
