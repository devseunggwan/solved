N = int(input())+1
for i in range(N-1):
    print(" " * i + "*" * ((2 * (N-i-1)) - 1))
