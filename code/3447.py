while True:
    try:
        S = input()
        while "BUG" in S: S = S.replace("BUG", "")
        print(S)
    except:
        break