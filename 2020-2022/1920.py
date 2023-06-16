import sys
import collections

N, NN, M = sys.stdin.readline(), dict(collections.Counter(
    map(int, sys.stdin.readline().strip().split()))), sys.stdin.readline()
for i in map(int, sys.stdin.readline().strip().split()):
    if(i not in NN.keys()):
        print(0)
    else:
        print(1)
