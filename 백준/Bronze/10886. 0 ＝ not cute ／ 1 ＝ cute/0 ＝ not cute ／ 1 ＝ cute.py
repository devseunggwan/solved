N = int(input())
print(f"Junhee is {'' if sum([int(input()) for _ in range(N)])/N > 0.5 else 'not '}cute!")