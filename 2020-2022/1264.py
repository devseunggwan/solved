import sys
import re

r = lambda: sys.stdin.readline()

M = ["a", "e", "i", "o", "u"]

while True:
    S = r().strip().lower()

    if S == "#":
        break

    print(sum([len(re.compile(i).findall(S)) for i in M]))
