₩T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    l1, l2, l3 = ((x2-x1)**2 + (y2-y1)**2) ** 0.5, (r1 + r2), abs(r2 - r1)
    if(x1 == x2 and y1 == y2 and r1 == r2):
        print(-1)
    elif(x1 == x2 and y1 == y2 and r1 != r2):
        print(0)

    elif(l1 < l2 and l1 > l3):
        print(2)
    elif(l1 == l2 or l1 == l3):
        print(1)
    else:
        print(0)
