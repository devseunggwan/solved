import math

input()
Y, M = 0, 0
for case in [int(i) for i in map(int, input().strip().split())]:
    Y += 10 * math.ceil(case // 30 + 1)
    M += 15 * math.ceil(case // 60 + 1)

if(Y == M): print("Y M {value}".format(value=Y))
elif(Y < M): print("Y {value}".format(value=Y))
else:print("M {value}".format(value=M))