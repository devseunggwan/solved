import sys

input = sys.stdin.readline
answer = 0

while True:
    N = int(input())

    if N == -1:
        break

    answer += N

print(answer)
