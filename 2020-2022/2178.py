N, M = map(int, input().strip().split())
L = [list(input()) for i in range(N)]
Z = [[0 for i in range(M)] for j in range(N)]
dx, dy, queue, Z[0][0] = [-1, 0, 1, 0], [0, -1, 0, 1], [[0, 0]], 1
ans = 1

while queue:
    x, y = queue.pop(0)
    for i in range(4):
        vx, vy = x + dx[i], y + dy[i]
        if(0 <= vx < N and 0 <= vy < M and L[vx][vy] == "1" and Z[vx][vy] == 0):
            queue.append([vx, vy])
            Z[vx][vy] = Z[x][y] + 1


print(Z[N-1][M-1])
