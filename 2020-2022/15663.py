import itertools

N, M = map(int, input().split())
L = list(map(int, input().strip().split()))
for i in sorted(set(itertools.permutations(L, M))): print(*i)