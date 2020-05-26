N = int(input())
M, ans = 1, 0
for i in range(1, N+1):
    M *= i

for j in range(len(str(M))-1, -1, -1):
    if(str(M)[j] == "0"):
        ans += 1
    else:
        break
print(ans)
