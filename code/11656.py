S = input()

for j in sorted([S[i:] for i in range(len(S))]):
    print(j)