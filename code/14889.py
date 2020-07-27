from itertools import combinations, permutations

N = int(input())
M = [list(map(int, input().strip().split())) for _ in range(N)]
V = list(combinations([i for i in range(N)], N//2))
ans = list()


for W in range(len(V)//2):
    A = list(permutations(V[W], 2))
    B = list(permutations(V[-W-1], 2))

    aSum, bSum = 0, 0

    for p in A: aSum += M[p[0]][p[1]]
    for q in B: bSum += M[q[0]][q[1]]

    ans.append(abs(aSum - bSum))
    
print(min(ans))