V = 0

for i in input():
    
    if(V == 4): break
    if((i == "U" and V == 0) or (i == "C" and (V == 1 or V == 3)) or (i == "P" and V == 2)):
        V += 1
    
    
if(V == 4): print("I love UCPC")
else: print("I hate UCPC")