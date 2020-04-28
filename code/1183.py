import sys

ans = [[j[1]-j[0]for j in list(map(int, sys.stdin.readline().strip().split()))]
       for i in range(int(input()))]
print(len(set(ans)))
