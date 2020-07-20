cnt = 1
while True:
    L, P, V = map(int, input().strip().split())

    if(L == 0 and P == 0 and V == 0): break
    if(V%P < L): print("Case {}: {}".format(cnt, ((V//P)*L) + V%P))
    else: print("Case {}: {}".format(cnt, ((V//P)*L) + L))
    cnt += 1