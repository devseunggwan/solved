c = [1,1,2,2,2,8]
C = [i for i in map(int, input().split())]
for i, j in zip(c, C): print(i-j, end=" ")