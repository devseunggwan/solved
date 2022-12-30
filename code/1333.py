N, L, D = map(int, input().strip().split())
called = 0
M = []

for i in range(N):
    M.extend([1] * L)
    M.extend([0] * 5)

for i in range(D, len(M), D):
    if M[i] == 0:
        print(i)
        called = 1
        break

if not called:
    print(D * (((len(M) - 5) // D) + 1))
