from collections import Counter

P = []

for i in range(int(input())):
    X = dict(Counter(map(int, input().strip().split())))

    if(list(X.values())[0] == 3):
        P.append(10000 + 1000*list(X.keys())[0])
    elif(max(list(X.values())) == 2):
        P.append(1000 + 100 * list(X.keys())
                 [list(X.values()).index(max(list(X.values())))])
    else:
        P.append(100 * max(list(X.keys())))

print(max(P))
