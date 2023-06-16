N = int(input())
S = list(map(int, input().strip().split()))
T = [False]*100
ans = 0
for i in range(N):
    if(T[S[i]-1] == False):
        T[S[i]-1] = True
    else:
        ans += 1

print(ans)
