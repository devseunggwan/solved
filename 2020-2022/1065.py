N = int(input())
ans = 0
for i in range(1, N+1):
    if(i < 100):
        ans += 1
    else:
        M = str(i)
        if(int(M[1]) - int(M[0]) == int(M[2]) - int(M[1])):
            ans += 1

print(ans)
