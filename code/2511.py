A, B, P, W = list(map(int, input().strip().split())), list(
    map(int, input().strip().split())), [0, 0], ""

for i, j in zip(A, B):
    if(i == j):
        P[0] += 1
        P[1] += 1
    elif(i > j):
        P[0] += 3
        W = "A"
    else:
        P[1] += 3
        W = "B"


print(P[0], P[1])
if(P[0] == 10):
    print("D")
elif(P[0] == P[1]):
    print(W)
elif(P[0] > P[1]):
    print("A")
else:
    print("B")
