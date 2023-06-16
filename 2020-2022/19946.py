N = 18446744073709551616 - int(input())

for i in range(64):
    if(2**i == N): 
        print(64-i)
        break