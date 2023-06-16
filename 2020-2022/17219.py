import sys

N, M = map(int, sys.stdin.readline().strip().split())
T = dict()
for _ in range(N):
    site, pw = map(str, sys.stdin.readline().strip().split())
    T[site] = pw

for _ in range(M):
    print(T[sys.stdin.readline().strip()])
