M = [list(map(int, input().split())) for _ in range(int(input()))]
M = sorted([A-B for A, B in M])
print(1 if len(M) % 2 else M[len(M)//2] - M[len(M)//2-1] + 1)
