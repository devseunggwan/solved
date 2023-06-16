a, b, c = 0, 1, int(input())
f = 1000000000 // 10 * 15

if(c % 2 == 0 and c < 0):
    print(-1)
elif(c == 0):
    print(0)
else:
    print(1)

c = abs(c)

if(c == 0):
    print(0)
else:
    for i in range((c % f)-1):
        a, b = b, (a+b) % 1000000000
    print(b)
