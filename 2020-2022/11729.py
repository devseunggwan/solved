import sys
import heapq

N = int(sys.stdin.readline().strip())
H = []

for i in range(N):
    M = int(sys.stdin.readline().strip())
    if(M == 0 and len(H) > 0):
        print(heapq.heappop(H)[1])
    elif(M == 0 and len(H) == 0):
        print(0)
    else:
        heapq.heappush(H, (-M, M))
