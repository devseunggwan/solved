for T in range(int(input())):
    N = input().strip().split()
    M = float(N[0])

    for i in range(1, len(N)):
        if(N[i] == "@"): M *= 3
        elif(N[i] == "%"): M += 5
        elif(N[i] == "#"): M -= 7
    
    print("{:.2f}".format(M))