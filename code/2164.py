N = int(input())
M = [False]*N
SW = True
log = []
while False in M:
    for i in range(N):
        if(M[i] == True):
            continue
        elif(M[i] == False and SW == True):
            M[i] = True
            SW = False
            log.append(i)
        elif(M[i] == False and SW == False):
            SW = True
print(log[-1]+1)
