n = int(input())
L = [1, 3]
for i in range(2, n+1):
    L.append(((L[-2] * 2) + L[-1]) % 10007)
print(L[n-1])
