N = int(input())
L = list(map(int, input().strip().split()))
ans, sums = 0, sum(L)

for i in L: ans+= (sums-i)*i

print(ans//2)