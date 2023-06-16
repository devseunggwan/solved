a, b, c = 0, 1, int(input())
if(c == 0):
    print(0)
else:
    for i in range(c-1):
        a, b = b, a+b
    print(b)
