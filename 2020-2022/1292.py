A, B = map(int, input().strip().split())

ans = []
for i in range(50):
    for j in range(i):
        ans.append(i)
print(sum(ans[A-1:B]))
