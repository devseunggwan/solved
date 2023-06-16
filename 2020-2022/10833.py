ans = 0
for T in range(int(input())):
    a, b = map(int, input().strip().split())
    ans += b%a
print(ans)
