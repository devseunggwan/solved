T = int(input())

for i in range(T):
    P = ""
    for S in input().strip().split():
        P += "{} ".format(S[::-1])
    print(P.strip())
