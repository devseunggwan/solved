import sys

R = lambda: sys.stdin.readline()
N, M = map(int, R().strip().split())

V = [list(R().strip()) for x in range(N)]

ans = 1

for i in range(1, min(N, M)):
    for fN in range(N - i):
        if ans == (i + 1) ** 2:
            break
        for fM in range(M - i):
            if V[fN][fM] == V[fN + i][fM] == V[fN][fM + i] == V[fN + i][fM + i]:
                ans = (i + 1) ** 2
                break

print(ans)
