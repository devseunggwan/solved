cnt = int(input())
A = [i for i in map(int, input().strip().split())]

print(min(A) * max(A))
