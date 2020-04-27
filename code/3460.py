T = int(input())
for i in range(T):
    n = bin(int(input()))[2:]
    K = 0
    for x in range(len(n)-1, -1, -1):
        if(n[x] == "1"):
            print(K, end=" ")
        K += 1
