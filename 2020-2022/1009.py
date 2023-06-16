for loop in range(int(input())):
    a, b = map(int, input().strip().split())
    V, W = bin(b)[2:], []
    if(a == 1): 
        print(1)
        continue
    elif(a%10 == 0):
        print(10)
        continue

    for B in range(len(V)):
        if(V[B] is "1"): W.append(len(V)-1-B)
    
    W.sort()

    mods = [a%10]
    for i in range(1, W[-1]+1):
        new = (mods[i-1] ** 2) % 10
        mods.append(new)
    
    exps = 1
    for c in W: exps = exps * mods[c]
    
    if(exps%10 == 0): print(10)
    else: print(exps%10) 