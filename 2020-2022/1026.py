ans = 0
num, A, B = int(input()), sorted(list(map(int, input().strip().split()))), sorted(
    list(map(int, input().strip().split())), reverse=True)
for i in zip(A, B):
    ans += i[0]*i[1]
print(ans)
