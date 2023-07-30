N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())
    ad = e - (r + c)
    
    if ad > 0:
        print("advertise")
    elif ad < 0:
        print("do not advertise")
    else:
        print("does not matter")