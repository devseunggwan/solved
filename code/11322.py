def factorial(n, y, z):
    N = y
    for i in range(n, 0, -1):
        N *=i
        if(N > ((10**8)*z)): return True

    return False

Big = {
    "O(N)": lambda x, y, z: (x*y) > ((10**8)*z),
    "O(N^2)": lambda x, y, z: ((x**2)*y) > ((10**8)*z),
    "O(N^3)": lambda x, y, z: ((x**3)*y) > ((10**8)*z),
    "O(2^N)": lambda x, y, z: ((2**x)*y) > ((10**8)*z),
    "O(N!)": lambda x, y, z: factorial(x, y, z)}

for _ in range(int(input())):
    O, N, T, L = input().strip().split()
    if((Big[O](int(N), int(T), int(L)))): print("TLE!")
    else: print("May Pass.")
