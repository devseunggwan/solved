import sys
R = lambda: map(int, sys.stdin.readline().strip().split())

N, M = R()

S = [0] + list(R())
for idx in range(1, N+1):
    S[idx] += S[idx-1]

TC = [R() for _ in range(M)]
[print(S[j] - S[i-1]) for i, j in TC]
