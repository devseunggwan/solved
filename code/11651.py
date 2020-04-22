import sys

for j in sorted([[int(i) for i in map(int, sys.stdin.readline().strip().split())]
                 for i in range(int(input()))], key=lambda x: (x[1], x[0])):
    print(j[0], j[1])
