import sys

N, M = map(int, sys.stdin.readline().strip().split())
AL = []
AD = {}

for i in range(1, N+1):
    K = str(sys.stdin.readline().strip())
    AL.append(K)
    AD[K] = i

for i in range(M):
    Q = sys.stdin.readline().strip()
    if(Q.isdigit()):
        print(AL[int(Q)-1])
    else:
        print(AD[Q])
