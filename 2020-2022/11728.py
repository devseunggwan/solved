A, B = map(int, input().strip().split())
M = sorted(list(map(int, input().strip().split())) +
           list(map(int, input().strip().split())))
for i in range(A+B):
    if(i == A+B-1):
        print(M[i])
    else:
        print(M[i], end=" ")
