import sys


def read():
    r = sys.stdin.readline

    N, K = map(int, r().strip().split())
    M = [int(r()) for _ in range(N)]

    return N, K, M


def get_answer(K, M):
    start = 0
    end = max(M)
    
    while start + 1 != end:
        mid = (start + end) // 2
        if mid == 0:
            return 0, 0
        
        resp = sum([pod // mid for pod in M])
        
        if resp >= K:
            start = mid
        else:
            end = mid
    
    return start, end


if __name__ == "__main__":
    N, K, M = read()
    start, end = get_answer(K, M)
    
    if start + end == 0:
        print(0)
    else:
        answer = end if sum([pod // end for pod in M]) == K else start
        print(answer)
