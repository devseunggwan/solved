N = [list(map(str, input().strip().split())) for i in range(int(input()))]
M = sorted([[i[0], int(i[1]), int(i[2]), int(i[3])]
            for i in N], key=lambda x: (x[3], x[2], x[1]))
print(M[-1][0])
print(M[0][0])
