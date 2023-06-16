N, F = int(input()), int(input())

for i in range(100):
    T = ((N//100) * 100) + i
    if(T % F == 0):
        print(str(T)[-2:])
        break
