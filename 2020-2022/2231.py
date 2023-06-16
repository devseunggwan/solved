N = int(input())
res = 0


for n in range(N):
    lst_num = [int(i) for i in str(n)]
    lst_num.append(n)

    if sum(lst_num) == N:
        res = n
        break

print(res)
