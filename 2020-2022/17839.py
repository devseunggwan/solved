from collections import deque

Baba, D, ans = "", dict(), set()
T = deque()

for _ in range(int(input())):
    P, Q = input().strip().split(" is ")
    if(P == "Baba"): 
        T.append(Q)
        ans.add(Q)
    else: D[P] = Q

while T:
    if(T[0] not in D.keys()): break
    ans.add(D[T[0]])
    T.append(D[T[0]])
    T.popleft()

for i in sorted(list(ans)):
    print(i)