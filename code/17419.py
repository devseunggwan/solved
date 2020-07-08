import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

nor, spc, sev = dict(), dict(), list()

for _ in range(A):
    V, W = sys.stdin.readline().strip().split()
    nor[V] = int(W)

for _ in range(B):
    V, W = sys.stdin.readline().strip().split()
    spc[V] = int(W)

sev = [sys.stdin.readline().strip() for _ in range(C)]

N = int(sys.stdin.readline().strip())
M = [sys.stdin.readline().strip() for _ in range(N)]

chk = [0 for i in range(3)]

for i in M:
    if(i in nor.keys()): 
        chk[0] += nor[i]
    elif(i in spc.keys()): 
        chk[1] += spc[i]
    elif(i in sev and chk[2] == 0): 
        chk[2] += 1
    else:
        chk[2] += 1
        break

if(chk[0] < 20000 and chk[1] > 0): print("No")
elif(chk[0]+chk[1] < 50000 and chk[2] > 0): print("No")
elif(chk[2] > 1): print("No")
else: print("Okay")