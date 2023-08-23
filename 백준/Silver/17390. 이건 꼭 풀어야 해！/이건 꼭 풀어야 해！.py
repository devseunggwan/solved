import sys
r = lambda: map(int, sys.stdin.readline().strip().split())

def preprocess(arr):
    # 누적 합을 계산합니다.
    cumulative_sum = [0]
    
    for num in arr:
        cumulative_sum.append(cumulative_sum[-1] + num)

    return cumulative_sum

def calculate_range_sum(cumulative_sum, start, end):
    # 구간 합을 계산합니다.
    range_sum = cumulative_sum[end] - cumulative_sum[start]

    return range_sum

if __name__ == "__main__":
    A, Q = r()
    M = list(r())
    M.sort()
    M = preprocess(M)

    for _ in range(Q):
        L, R = r()
        print(calculate_range_sum(M, L-1, R))