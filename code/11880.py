import sys

for T in range(int(input())):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    print(a**2+b**2+c**2+min(a*b, b*c, c*a)*2)