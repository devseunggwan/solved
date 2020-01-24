a, b = map(int, input().split())
c, d = a, b
while(b != 0): a, b = b, a%b

print(a)
print(int((c*d)/a))