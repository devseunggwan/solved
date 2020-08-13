N = int(input())
M = sorted(list(set(map(int, input().strip().split()))))
print(*M)