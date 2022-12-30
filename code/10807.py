import sys
from collections import Counter


def read():
    return sys.stdin.readline().strip()


int(read())
print(Counter(read().split())[read()])
