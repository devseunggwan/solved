import sys


def read():
    return sys.stdin.readline().strip()


for _ in range(int(read())):
    C = read()
    print(f"{C[0]}{C[-1]}")
