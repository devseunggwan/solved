import sys

N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

res = 0
start = 0
end = max(H)

while start <= end:
    mid = (start + end) // 2
    total = sum([height - mid if height > mid else 0 for height in H])

    if total < M:
        end = mid - 1

    else:
        res = mid
        start = mid + 1

print(res)
