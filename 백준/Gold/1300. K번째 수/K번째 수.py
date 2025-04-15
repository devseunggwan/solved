def read() -> tuple[int, int]:
    N = int(input())
    k = int(input())

    return N, k

def solve(N: int, k: int) -> int:
    left, right = 1, N * N
    
    while left < right:
        mid = (left + right) // 2
        count = 0
        
        for i in range(1, N + 1):
            count += min(mid // i, N)
        
        if count < k:
            left = mid + 1
        else:
            right = mid

    return left

def main():
    N, k = read()
    answer = solve(N, k)

    print(answer)    


if __name__ == "__main__":
    main()
