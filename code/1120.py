A, B = input().strip().split()
ans = list()
for i in range(len(B)-len(A)+1):
    dif = 0
    for a, b in zip(A, B[i:len(A)+i]):
        if(a != b): dif += 1
    ans.append(dif)
print(min(ans))