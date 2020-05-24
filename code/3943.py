import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    L = list()
    n = int(sys.stdin.readline().strip())
    ans = 1
    while (n is not 1):
        ans = max(ans, n)
        n = n//2 if n % 2 == 0 else (n*3) + 1

    print(ans)
