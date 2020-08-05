A, B = map(int, input().strip().split())
C, D = map(int, input().strip().split())
E, F = A*D+B*C, B*D
G, H= E, F

while H != 0:
    G, H = H, G%H

print(E//G, F//G)