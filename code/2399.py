N = int(input())
X = sorted(list(map(int, input().strip().split())))
print(abs(sum([X[i] * (2 * i - N + 1) for i in range(len(X))])) * 2)
