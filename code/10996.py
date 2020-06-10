N = int(input())

if(N == 1):
    print("*")
else:
    for i in range(N):
        if(N%2 == 0):
            print(("* " * (N//2)).strip())
            print((" *" * (N//2)))
        else:
            print(("* " * (N//2 + 1)).strip())
            print((" *" * (N//2)))