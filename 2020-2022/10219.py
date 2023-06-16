T = int(input())
for _ in range(T):
    H, W = map(int, input().strip().split())
    M = reversed([input() for i in range(H)])

    for i in M:
        print(i)