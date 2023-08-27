import sys
from collections import deque

R = lambda: map(int, sys.stdin.readline().split())

n, m = R()
T = [list(R()) for _ in range(n)]
path = [[0] * m for _ in range(n)]
start = (0, 0)
queue = deque([])

ROUTE = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for i in range(n):
    for j in range(m):
        if T[i][j] == 2:
            start = (i, j)
            queue.append(start)
            break

while queue:
    node = queue.popleft()
    
    for r in ROUTE:
        y, x = node[0] + r[0], node[1] + r[1]
        
        if -1 < y < n and -1 < x < m and (y, x) != start and path[y][x] == 0 and T[y][x]:
            queue.append((y, x))
            path[y][x] = path[node[0]][node[1]] + 1

for i in range(n):
    for j in range(m):
        if T[i][j] and path[i][j] == 0 and start != (i, j):
            path[i][j] = -1

[print(" ".join(map(str, P))) for P in path]