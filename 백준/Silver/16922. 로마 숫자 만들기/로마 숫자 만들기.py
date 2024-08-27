from itertools import combinations_with_replacement

N = int(input())
M = [1, 5, 10, 50]

print(len(set([sum(i) for i in list(combinations_with_replacement(M, N))])))
