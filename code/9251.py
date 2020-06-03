X, Y = input().strip(), input().strip()
M = [[0 for i in range(len(Y) + 1)] for j in range(len(X) + 1)]

for i in range(1, len(X) + 1):
    for j in range(1, len(Y) + 1):
        if(X[i-1] == Y[j-1]):
            M[i][j] = M[i - 1][j - 1] + 1
        else:
            M[i][j] = max(M[i][j-1], M[i-1][j])

print(M[-1][-1])
