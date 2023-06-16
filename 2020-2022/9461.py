T = int(input())

L = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(9, 100):
    L.append(L[i] + L[i-4])

for _ in range(T):
    print(L[int(input()) - 1])
