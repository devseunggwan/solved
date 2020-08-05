from collections import deque

for i in range(3):
    A = deque()
    M = list(map(int, input().strip().split()))
    
    if(M[5] - M[2] < 0):
        A.append(M[5]-M[2]+60)
        M[4] -= 1
    else:
        A.append(M[5]-M[2])
    if(M[4] - M[1] < 0):
        A.appendleft(M[4]-M[1]+60)
        M[3] -= 1
    else:
        A.appendleft(M[4]-M[1])
    A.appendleft(M[3]-M[0])
    print(*list(A))