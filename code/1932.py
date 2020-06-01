L = [list(map(int, input().split())) for i in range(int(input()))]

for i in range(1, len(L)):
    for j in range(len(L[i])):
        if(j == 0):
            L[i][j] += L[i-1][0]
        elif(j == len(L[i]) - 1):
            L[i][j] += L[i-1][-1]
        else:
            L[i][j] += max(L[i-1][j-1], L[i-1][j])


print(max(L[-1]))
