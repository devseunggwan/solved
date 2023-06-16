import sys

K, N = map(int, sys.stdin.readline().strip().split())
M = [int(sys.stdin.readline()) for i in range(K)]
start, end = 1, max(M)
while start <= end:
    mid = (start + end)//2
    O = 0
    for i in M:
        O += i//mid
    if(O >= N):
        start = mid + 1
    else:
        end = mid - 1

print(end)
