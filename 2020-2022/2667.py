N = int(input())
M = [[int(j) for j in input()] for i in range(N)]
ans = []

def dfs(M, N, cnt ,x, y):
    M[x][y] = 0 
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        vx = x + dx[i]
        vy = y + dy[i]

        if (vx >= 0 and vx < N and vy >= 0 and vy < N and M[vx][vy] == 1):
            cnt = dfs(M, N, cnt + 1, vx, vy)
        
    return cnt

for i in range(N):
    for j in range(N):
        if(M[i][j] == 1): ans.append(dfs(M, N, 1, i, j))

print(len(ans))
for i in sorted(ans): print(i)