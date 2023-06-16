from collections import Counter

A, P = map(int, input().strip().split())
slc = A
N = [A]
for i in range(1000):
    num = 0
    for j in str(slc):
        num += int(j)**P
    slc = num
    N.append(num)
ans = 0
N = dict(Counter(N))
for i in N:
    if(N[i] == 1):
        ans += 1

print(ans)
