from collections import deque


N, K = map(int, input().strip().split())
Q, T = deque([N]), [0 for i in range(100001)]


while Q:
    V = Q.popleft()
    if(V == K):
        print(T[V])
        break
    for R in (V-1, V+1, V*2):
        if(0<=R<100001 and not T[R]):
            T[R] = T[V] + 1
            Q.append(R)