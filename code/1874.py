import sys
from collections import deque

N = int(sys.stdin.readline())
M = deque([int(sys.stdin.readline()) in range(N)])
L = 1
while M:
    if(M[0] - L == 0):
        pass
    elif(M[0] - L > 0):
        pass
    elif(M[0] - L < 0):
        pass