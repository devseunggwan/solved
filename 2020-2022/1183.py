import sys

ans = set()

for i in range(int(input())):
    A, B = map(int, sys.stdin.readline().strip().split())
    ans.add(A-B)

print(ans)
print(len(ans))
