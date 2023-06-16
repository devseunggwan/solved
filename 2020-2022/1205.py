import sys

R = lambda: sys.stdin.readline()
N, S, P = map(int, R().split())
M = list(map(int, R().split()))

if(P == 0): print(-1)
elif(N == 0): print(1) 
else:
    M.append(S)
    M.sort(reverse=True)
    sol = M.index(S)+1
    if(sol > P): print(-1)
    else:
        if(S==M[-1] and N==P): print(-1) 
        else: print(sol)