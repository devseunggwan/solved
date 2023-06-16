M = [int(input()) for i in range(int(input()))]

if(M[1]-M[0] == M[2]-M[1]):
    print(M[-1] + M[1] - M[0])
else:
    print(M[-1] * (M[1]//M[0]))