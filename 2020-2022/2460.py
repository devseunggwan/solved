X, Y = 0, []

for i in [list(map(int, input().strip().split())) for j in range(10)]:
    X += i[1] - i[0]
    Y.append(X)

print(max(Y))
