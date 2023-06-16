import sys
K = []
for i in range(int(input())):
    O = sys.stdin.readline().strip().split()
    O[0] = int(O[0])
    K.append(O)

for i in sorted(K, key=lambda x: x[0]):
    print(i[0], i[1])
