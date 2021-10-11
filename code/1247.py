import sys

r = lambda: sys.stdin.readline()

for _ in range(3):
    case = sum([int(r()) for __ in range(int(r()))])

    if case > 0:
        print("+")
    elif case < 0:
        print("-")
    else:
        print("0")
