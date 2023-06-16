from collections import deque

N, M = map(int, input().split())
Q = deque([i for i in range(1, N+1)])
L = deque(list(map(int, input().split())))
ans = 0

while L:
    if(Q.index(L[0]) > len(Q)//2):
        for i in range(len(Q) - Q.index(L[0])):
            Q.appendleft(Q.pop())
            ans += 1
    else:
        for i in range(Q.index(L[0])):
            Q.append(Q.popleft())
            ans += 1

    L.popleft()
    Q.popleft()
print(ans)
