N = int(input())
M = [[0, []] for i in range(N + 1)]
M[1][1] = [1]
for i in range(2, N + 1):
    M[i][0] = M[i-1][0] + 1
    M[i][1] = M[i-1][1] + [i]
    if(i % 2 == 0 and M[i][0] > M[i//2][0] + 1):
        M[i][0] = M[i//2][0] + 1
        M[i][1] = M[i//2][1] + [i]
    if(i % 3 == 0 and M[i][0] > M[i//3][0] + 1):
        M[i][0] = M[i//3][0] + 1
        M[i][1] = M[i//3][1] + [i]

print(M[-1][0])
print(*sorted(M[-1][1], reverse=True))
