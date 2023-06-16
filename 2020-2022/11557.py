for i in range(int(input())):
    N = list()
    
    for j in range(int(input())):
        A, B = input().split()
        N.append([int(B), A])

    N = sorted(N, reverse=True)

    print(N[0][1])