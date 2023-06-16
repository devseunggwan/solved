L = list()

for i in [int(input()) for i in range(7)]:
    if(i % 2 == 1):
        L.append(i)

if(not L):
    print(-1)
else:
    print(sum(L))
    print(min(L))
