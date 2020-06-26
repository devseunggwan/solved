M, D = int(input()), int(input())
if(M == 2 and D == 18): print("Special")
elif(M > 2 or (M == 2 and D > 18)): print("After")
elif(M < 2 or (M == 2 and D < 18)): print("Before")