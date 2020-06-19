N = int(input())
S = [input() for i in range(N)]

for i in range(N):
    R = S[i][::-1]
    for j in range(i, N):
        if(R == S[j]):
            print(len(R), R[len(R)//2])
    