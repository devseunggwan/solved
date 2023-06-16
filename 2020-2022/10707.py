W = [int(input()) for i in range(5)]
if(W[4] <= W[2]):
    B = W[1]
else:
    B = W[1]+((W[4]-W[2])*W[3])
print(min(W[0]*W[4], B))
