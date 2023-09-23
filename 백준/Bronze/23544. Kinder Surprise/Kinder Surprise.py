from collections import Counter

N = int(input())
print(N - len(Counter([input() for _ in range(N)])))
