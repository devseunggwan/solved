def solution():
    N, M = map(int, input().strip().split())
    H = sorted([[listen for listen in map(int, input().strip().split())] for loop in range(N)])

    for i in range(1, N):
        for j in range(M):
            if(H[i-1][j] > H[i][j]): return "NO"
    
    return "YES"

print(solution())