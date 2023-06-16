import math

N = int(input())
M = len(str(N))

for i in range(M-1):
    if(str(N)[-i-1] == "5"):
        N = math.ceil(N*(10**(-i-1)))*(10**(i+1))
    else: N = round(N, -i-1)
print(N)