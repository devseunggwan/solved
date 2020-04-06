W = [int(input()) for i in range(2)]
if(W[0]>0 and W[1]>0): print(1)
elif(W[0]<0 and W[1]>0): print(2)
elif(W[0]<0 and W[1]<0): print(3)
else: print(4)
