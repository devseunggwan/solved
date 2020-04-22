import sys
import collections


def r(): return sys.stdin.readline()


N = int(r())
M = sorted([int(r()) for i in range(N)])
O = collections.Counter(M).most_common()
print(round(sum(M)/N))
print(M[N//2])
if(len(O) == 1):
    print(O[0][0])
else:
    if(O[0][1] == O[1][1]):
        print(O[1][0])
    else:
        print(O[0][0])
print(M[-1]-M[0])
