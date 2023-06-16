while True:
    A = input()
    ans = []
    if(A == "#"): break
    for i in set(list(A)):
        s = i.lower()
        if(s.isalpha() and s not in ans):
            ans.append(s)
        if(len(ans) == 26): break
    
    print(len(ans))