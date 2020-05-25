a, b, c = 0, 1, int(input())
f = 1000000 // 10 * 15
if(c == 0):
    print(0)
else:
    for i in range((c % f)-1):
        a, b = b, (a+b) % 1000000
    print(b)
