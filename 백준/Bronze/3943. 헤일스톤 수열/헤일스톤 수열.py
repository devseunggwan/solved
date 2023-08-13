import sys

r = lambda: sys.stdin.readline()

for _ in range(int(r())):
    n = int(r())

    answer = 1
    
    while (n is not 1):
        answer = max(answer, n)
        n = (n * 3) + 1 if n % 2 else n // 2 
    
    print(answer)