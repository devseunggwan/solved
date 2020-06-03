from collections import deque

T = int(input())

for _ in range(T):
    K = input().strip()
    L, R = deque(), deque()

    for i in K:
        if(i == "-"):
            if(len(L) > 0):
                L.pop()
        elif(i == "<"):
            if(len(L) > 0):
                R.appendleft(L.pop())
        elif(i == ">"):
            if(len(R) > 0):
                L.append(R.popleft())
        else:
            L.append(i)

    ans = ""
    for i in L:
        ans += i
    for i in R:
        ans += i
    print(ans)
