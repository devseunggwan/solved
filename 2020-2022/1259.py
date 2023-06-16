while True:
    M, ans = input(), "yes"
    if(M == "0"):
        break
    else:
        for i in range(len(M)//2):
            if(M[i] != M[-(i+1)]):
                ans = "no"
                break

    print(ans)
