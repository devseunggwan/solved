n, k = map(int, input().strip().split())
r = 0
if(n > k): r = k*(n-k)
m = k ** 0.5
for i in range(1, int(m)+1):
    a, b = min(k/i, m), k/(i+1)+1
    if(a < b): continue
    r += k*(a-b+1)-(a-b)*(a-b+1)*i/2

print(m/k)

for i in range(1, int(min(m/k+1, n)+1)): r += k%i

print(r)
