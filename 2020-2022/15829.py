L, H, ans = int(input()), input(), 0

for i in range(L):
    ans += (ord(H[i])-96) * (31**i)
print(ans % 1234567891)
