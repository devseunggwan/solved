import re

io = input()
happy = len(re.compile("\:\-\)").findall(io))
sad = len(re.compile("\:\-\(").findall(io))

if(happy == 0 & sad == 0): print("none")
elif(happy == sad): print("unsure")
elif(happy > sad): print("happy")
else: print("sad")