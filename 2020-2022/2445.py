N = int(input())+1
for i in range(N):
    if(i == 0):
        continue
    print("*" * i + " " * (((2 * (N - i) - 1)) - 1) + "*" * i)

for i in range(N-1):
    if(i == 0):
        continue
    print("*" * (N-i-1) + " " * 2 * i + "*" * (N-i-1))
