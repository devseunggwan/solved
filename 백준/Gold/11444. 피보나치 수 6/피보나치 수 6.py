def mat_mul(A1, A2):
    return [
        [
            (A1[0][0]*A2[0][0]+A1[0][1]*A2[1][0]) % 1_000_000_007,
            (A1[0][0]*A2[0][1]+A1[0][1]*A2[1][1]) % 1_000_000_007
        ],
        [
            (A1[1][0]*A2[0][0]+A1[1][1]*A2[1][0]) % 1_000_000_007, 
            (A1[1][0]*A2[0][1]+A1[1][1]*A2[1][1]) % 1_000_000_007
        ]
    ]

def power(A, n):
    if n == 1:
        return A
    else:
        A = power(A, n // 2)
        return mat_mul(mat_mul(A, A), ([[1, 1], [1, 0]] if n % 2 else [[1, 0], [0, 1]]))

if __name__ == "__main__":
    n = int(input())
    res = [[1, 1], [1, 0]]
    
    print(power(res, n)[0][1] % 1_000_000_007)
