import sys
R = lambda: map(int, sys.stdin.readline().split())


def square(N, M1, M2):
    res = [[0 for _ in range(N)] for _ in range(N)]
    
    for row in range(N):
        for col in range(N):            
            for idx in range(N):
                res[row][col] += (M1[row][idx] * M2[idx][col]) % 1000
            
            res[row][col] = res[row][col] % 1000
    
    return res

def power(M, B, I):
    if B == 1:
        return M
    else:
        M = power(M, B//2, I)
        if B % 2:
            M = square(N, square(N, M, M), I)
        else:
            M = square(N, M, M)

        return M

if __name__ == "__main__":
    N, B = R()
    M = [list(R()) for _ in range(N)]
    res = M.copy()

    [print(*list(map(lambda x: x % 1000, r))) for r in power(res, B, M)]
