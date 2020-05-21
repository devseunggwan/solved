N = int(input())
M = [0] * (N + 1)
for i in range(2, N + 1):
    M[i] = M[i-1] + 1
    if(i % 2 == 0):
        M[i] = min(M[i], M[i//2]+1)
    if(i % 3 == 0):
        M[i] = min(M[i], M[i//3]+1)
print(M[-1])
