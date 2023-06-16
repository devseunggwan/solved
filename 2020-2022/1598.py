A, B = map(int, input().strip().split())
W, H = (abs(A // 4 - B // 4)), (abs(A % 4 - B % 4))

if H == 0:
    print(W - 1)
else:
    print(W + H)
