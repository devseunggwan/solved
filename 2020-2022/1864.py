N = {"-":0, "\\":1, "(": 2, "@": 3, "?":4, ">":5, "&": 6, "%":7, "/":-1}
while True:
    O, ans = list(input().strip()), 0
    O.reverse()
    print(O)
    if("#" in O): break
    for i, j in enumerate(O):
        if(i not in N.keys()): continue
        ans += N[j]*(8**i)
    print(ans)