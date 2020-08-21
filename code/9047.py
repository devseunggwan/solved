for T in range(int(input())):
    n, m = input(), 0

    while n != "6174":
        a, b = "", ""
        for i, j in zip(sorted(list(n), reverse=True), sorted(list(n))):
            a += i
            b += j
        

        n, m = str(int(a) - int(b)), m + 1

        if(len(n) <= 3):
            n = "0"*(4-len(n)) + n

    print(m)