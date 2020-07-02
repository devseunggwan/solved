A, B = map(int, input().strip().split())

def AB(A, B):
    cnt = 1
    while A < B:
        if(str(B)[-1] == "1"):
            B = int(str(B)[:-1])
            cnt += 1
        elif B % 2 == 0:
            B //=2
            cnt += 1
        elif B % 2 == 1:
            return -1
    
    if(A == B):
        return cnt
    else:
        return -1

print(AB(A, B))