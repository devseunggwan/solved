N, B = map(int, input().strip().split())
syn, ans = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", ""

while N != 0:
    ans = str(syn[N % B]) + ans
    N //= B

print(ans)
