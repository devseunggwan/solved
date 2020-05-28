N, M = map(int, input().split())

L = [[i + 1, False] for i in range(N)]
arr = []

def dfs(cnt):
    if(cnt == M):
        print(*arr)
        return

    for i in range(N):
        if(L[i][1]): continue

        L[i][1] = True
        arr.append(L[i][0])
        dfs(cnt + 1)
        arr.pop()
        L[i][1] = False

dfs(0)