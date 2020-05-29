for i in range(int(input())):
    N, M = map(int, input().strip().split())
    D, E = list(map(int, input().strip().split())), [i for i in range(N)]
    cnt = 0
    while D:
        if(D[0] == max(D)):
            if(E[0] == M):
                break
            cnt += 1
            D.pop(0)
            E.pop(0)
        else:
            D.append(D.pop(0))
            E.append(E.pop(0))

    print(cnt + 1)