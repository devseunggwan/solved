n = int(input())

def numBST(n: int):
    Tn = 0
    if(n == 0): return 1
    else:
        for i in range(1, n+1):
            Tn += numBST(i-1) * numBST(n-i)
    return Tn

print(numBST(n))