H, M, S = map(int, input().strip().split())
T = int(input())

M, S = M+T//60,  S+T % 60
M, S = M + S//60, S % 60
print((H + M//60) % 24, M % 60, S)
