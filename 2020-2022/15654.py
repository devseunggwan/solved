N, M = map(int, input().split())

L = sorted(list(map(int, input().strip().split())))
B = [False for i in range(N)]
arr = []

def dfs(cnt):
    if(cnt == M):
        print(*arr)
        return

    for i in range(N):
        if(B[i]): continue

        B[i] = True
        arr.append(L[i])
        dfs(cnt + 1)
        arr.pop()
        B[i] = False

dfs(0)