H, W = map(int, input().strip().split())

R = [input() for i in range(H)]
ans = []


def check(x, y):
    C1, C2 = 0, 0
    for h in range(x, x+8):
        for w in range(y, y+8):
            if(R[h][w] == "W" and w % 2 == 0 and h % 2 == 0):
                C1 += 1
            elif(R[h][w] == "W" and w % 2 == 1 and h % 2 == 0):
                C2 += 1
            elif(R[h][w] == "B" and w % 2 == 0 and h % 2 == 0):
                C2 += 1
            elif(R[h][w] == "B" and w % 2 == 1 and h % 2 == 0):
                C1 += 1
            elif(R[h][w] == "W" and w % 2 == 0 and h % 2 == 1):
                C2 += 1
            elif(R[h][w] == "W" and w % 2 == 1 and h % 2 == 1):
                C1 += 1
            elif(R[h][w] == "B" and w % 2 == 0 and h % 2 == 1):
                C1 += 1
            elif(R[h][w] == "B" and w % 2 == 1 and h % 2 == 1):
                C2 += 1
    ans.append(C1)
    ans.append(C2)


for X in range(H-7):
    for Y in range(W-7):
        check(X, Y)

print(min(ans))
