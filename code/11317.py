for T in range(int(input())):
    a, b, c, s, t = map(int, input().strip().split())
    if((b*b)-(4*a*c) < 0): print("Yes")
    elif(s <= (-b-(((b*b)-(4*a*c))**0.5))/2*a <= (-b+(((b*b)-(4*a*c))**0.5))/2*a <= t): print("Yes")
    else: print("No")