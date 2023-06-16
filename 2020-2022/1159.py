from collections import Counter
ans = []
N = int(input())
F = Counter([input()[0] for i in range(N)])
if(max(F.values()) < 5):
    print("PREDAJA")
else:
    for i in F.keys():
        if(F[i] > 4):
            ans.append(i)
    for _ in sorted(ans):
        print(_, end="")
