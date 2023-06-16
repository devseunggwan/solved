N = 1000 - int(input())
J = [500, 100, 50, 10, 5, 1]
ans = 0
for j in J:
    if(N == 0): break
    else:
        if(j <= N):
            ans += N//j
            N = N%j

print(ans)