for i in [[ent for ent in map(int, input().split())] for loop in range(int(input()))]:
    u, d = 1, 1
    for j in range(i[0], 0, -1):
        u *= i[1]+1-j
        d *= j
    print(int(u/d))