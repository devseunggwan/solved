N = int(input().strip())
F = list(map(int, input().strip().split()))
S = int(input().strip())

ans = 0

for f in F:
    if f != 0:
        if f % S == 0:
            ans += S * (f // S)
        else:
            ans += S * ((f // S) + 1)

print(ans)
