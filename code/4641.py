while True:
    V = list(map(int, input().strip().split()))
    if(-1 in V): break
    ans = 0
    for i in V[:-1]:
        if(i*2 in V): ans+=1
    print(ans)