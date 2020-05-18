while True:
    n = int(input())
    if(n == -1):
        break
    else:
        m = list()
        for i in range(1, n//2+1):
            if(n % i == 0):
                m.append(i)

        if(n == sum(m)):
            ans = "{} = 1".format(n)
            for i in range(1, len(m)):
                ans += " + {}".format(m[i])
            print(ans)
        else:
            print("{} is NOT perfect.".format(n))
