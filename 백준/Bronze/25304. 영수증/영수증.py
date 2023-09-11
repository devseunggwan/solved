mul = lambda x: x[0] * x[1]

X = int(input())
N = int(input())
Y = sum([mul(list(map(int, input().strip().split()))) for _ in range(N)])

print("Yes" if X == Y else "No")