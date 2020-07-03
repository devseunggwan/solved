R, C, ZR, ZC = map(int, input().strip().split())

V = [input() for i in range(R)]

for r in range(R):
    mer = ""
    for c in range(C):
        mer += V[r][c]*ZC
    for k in range(ZR):
        print(mer)