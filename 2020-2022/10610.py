N = sorted(list(input()), reverse=True)
S, ans = 0, ""


for i in N: 
    S += int(i)
    ans += i


if("0" not in N or S % 3 != 0): print(-1)
else: print(ans)