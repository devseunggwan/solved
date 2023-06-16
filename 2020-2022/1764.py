import sys

N, M = map(int, input().strip().split())
NS = set([sys.stdin.readline().strip() for i in range(N)])
NL = set([sys.stdin.readline().strip() for i in range(M)])

ans = sorted(NS.intersection(NL))
print(len(ans))
for i in ans:
    print(i)
