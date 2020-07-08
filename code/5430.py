from collections import deque

T = int(input())

for _ in range(T):
    Fnc = input()
    N = int(input())
    M = input()[1:-1]
    sw, rev = 0, 0
    
    if(M != ""): M = deque(map(int, M.strip().split(",")))
    else: M = deque(list())

    for i in Fnc:
        if(i == "R"):
            if(rev == 0):
                rev += 1
            else:
                rev -= 1
        if(i == "D"):
            if(M == deque()):
                sw += 1
                break
            else:
                if(rev == 0):
                    M.popleft()
                else:
                    M.pop()

    if(sw == 0):
        if(M == deque()):
            print([])
        else:
            if(rev == 1):
                M = (list(M)[::-1])
            ans = "["
            for V in range(len(M)):
                if(len(M)-1 == V): ans += "{}]".format(M[V])
                else: ans += "{},".format(M[V])
            print(ans)
    else: print("error")