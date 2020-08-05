N = int(input())
ans = 1

while N != 1:
    ans += 1
    if(N%2 == 0):
        N = N//2
    else:
        N = (3*N) + 1

print(ans)