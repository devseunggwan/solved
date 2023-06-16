P = input()
if(len(P)==1): print(1)
else:
	for i in range(int(len(P)/2)):
		if(P[i] != P[-(i+1)]): 
			print(0)
			break
		elif(i == int(len(P)/2)-1): 
			print(1)
			break
