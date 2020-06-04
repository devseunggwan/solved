import math

S = ['  *   ', ' * *  ', '***** ']


def star(n):
    for i in range(len(S)):
        S.append(S[i] + S[i])
        S[i] = "   " * n + S[i] + "   " * n


for i in range(int(math.log2((int(input())//3)))):
    star(int(pow(2, i)))

for i in S: print(i)