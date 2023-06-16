L, P = map(int, input().split())
for i in [j-L*P for j in map(int, input().split())]: print(i, end=" ")