N, M = map(int, input().strip().split())
V, W = 0, 0

X = [[v for v in input()] for _ in range(N)]

for i in range(N):
    if("X" not in X[i]): W += 1

for j in range(M):
    cnt = 0
    for i in range(N):
        if(X[i][j] == "X"): cnt+=1
    if(not cnt): V+=1

print(max(V, W))