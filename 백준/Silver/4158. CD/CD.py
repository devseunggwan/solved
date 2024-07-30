import sys

r = sys.stdin.readline

while True:
    N, M = map(int, r().strip().split())
    if N + M == 0:
        break
    
    answer = len(set(map(int, [r().strip() for _ in range(N)])) & set(map(int, [r().strip() for _ in range(M)])))
    
    print(answer)
