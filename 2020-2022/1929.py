M, N = map(int, input().strip().split())

def sol(i):
    if i == 1: return 0
    for j in range(2, int(i**0.5)+1):
        if(i%j == 0): return 0
    return 1

for i in range(M, N+1):
    if sol(i): print(i)