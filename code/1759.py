from itertools import combinations

L, C = map(int, input().strip().split())
M = sorted(input().strip().split())
M = combinations(M, L)
for i in M:
    V = len(set(i) - set(["a", "e", "i", "o", "u"]))
    if(V > 1 and V != L): 
        S = ""
        for j in list(i): S += j
        print(S)