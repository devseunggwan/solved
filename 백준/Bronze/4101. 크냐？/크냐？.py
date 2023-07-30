while True:
    testcase = input()
    
    if testcase == "0 0":
        break
        
    F, S = map(int, testcase.split())
    
    print("Yes" if F > S else "No")