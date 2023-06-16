import sys
import collections


N, NN, M = sys.stdin.readline(), dict(collections.Counter(
    map(int, sys.stdin.readline().strip().split()))), sys.stdin.readline()
for i in map(int, sys.stdin.readline().strip().split()):
    if(NN.get(i) == None):
        print(0, end=" ")
    else:
        print(NN.get(i), end=" ")
