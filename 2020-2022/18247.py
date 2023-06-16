for testcase in range(int(input())):
    H, W = map(int, input().strip().split())
    if(H < 12 or W < 4): print(-1)
    else: print(11*W + 4)