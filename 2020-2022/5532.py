import math

D = [int(input()) for i in range(5)]
print(D[0] - max(math.ceil(D[1]/D[3]), math.ceil(D[2]/D[4])))
