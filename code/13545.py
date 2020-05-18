N = int(input())
A = list(map(int, input().strip().split()))
M = int(input())

for i, j in [list(map(int, input().strip().split())) for _ in range(M)]:
    r = A[i-1:j]
    ans = 0
    for p in range(len(r)-1):
        for q in range(p+1, len(r)):
            if(sum(r[p:q+1]) == 0 and len(r[p:q+1]) > ans):
                ans = len(r[p:q+1])
    print(ans)
