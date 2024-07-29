N = int(input())
P = input().split()
M = int(input())
Q = input().split()

D = {x: "1" for x in set(P) & set(Q)}
print(" ".join([D.get(x, "0") for x in Q]))