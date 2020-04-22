import sys

N = int(sys.stdin.readline())
M = [int(sys.stdin.readline()) in range(N)]
V = [False] * N

val = 0

for i in M:
    if(val < i):
        for i in range(i-val):
            print("+")
        val = i
    else:
        pass
