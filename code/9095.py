T = int(input())
N, L = [int(input())-1 for i in range(T)], [1, 2, 4]
for i in range(4, 12):
    L.append(sum(L[-3:]))

for j in N:
    print(L[j])
