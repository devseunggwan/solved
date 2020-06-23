for _ in range(int(input())):
    S = input()
    TC = str(int(S) + int(S[::-1]))
    
    for i in range(len(TC)//2+1):
        if(TC[i] != TC[-i-1]): 
            print("NO")
            break
        elif(i == ((len(TC)//2) - 1)): 
            print("YES")
            break