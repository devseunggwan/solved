N, M = int(input()), list()
for i in range(N):
    A, B, C, D = input().strip().split()
    M.append([A, int(B), int(C), int(D)])

for i in sorted(M, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(i[0])
