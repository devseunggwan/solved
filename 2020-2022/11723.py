import sys

M = int(input())
S = [False]*20
for i in range(M):
    Q = sys.stdin.readline().strip().split()
    if(Q[0] == "add"):
        S[int(Q[1])-1] = True
    elif(Q[0] == "remove"):
        S[int(Q[1])-1] = False

    elif(Q[0] == "check"):
        if(S[int(Q[1])-1] == True):
            print(1)
        else:
            print(0)
    elif(Q[0] == "toggle"):
        if(S[int(Q[1])-1] == False):
            S[int(Q[1])-1] = True
        else:
            S[int(Q[1])-1] = False
    elif(Q[0] == "all"):
        S = [True]*20
    elif(Q[0] == "empty"):
        S = [False]*20
