L = [list(map(int, input().strip().split())) for i in range(int(input()))]
for i in range(1, len(L)):
    L[i][0], L[i][1], L[i][2] = min(L[i-1][1], L[i-1][2]) + L[i][0], min(
        L[i-1][0], L[i-1][2]) + L[i][1], min(L[i-1][0], L[i-1][1]) + L[i][2]
print(min(L[-1][0], L[-1][1], L[-1][2]))
