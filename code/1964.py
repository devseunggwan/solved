def pent(n):
    N = 5
    if(pent != 1):
        for i in range(2, n+1):
            N += (i+1)*3-2
    return N


print(pent(int(input())) % 45678)
