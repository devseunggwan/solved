N, K = map(int, input().strip().split())
M = [False]*N
ans = []
swt = 0


def Joshpus(K: int, member: list):
    global swt, ans
    for i in range(N):
        if(member[i]):
            continue
        elif(member[i] == False and swt == K-1):
            member[i] = True
            swt = 0
            ans.append(i+1)
        elif(member[i] == False and swt != K-1):
            swt += 1

    return member


while False in M:
    M = Joshpus(K, M)

print("<", end="")
for i in range(N):
    if(i == N-1):
        print(str(ans[i])+">", end="")
    else:
        print(str(ans[i])+",", end=" ")
