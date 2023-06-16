N = int(input())
K = int((2*N)**0.5 - 1)
while True:
    if(K*(K+1) > N*2):
        print(K-1)
        break
    else:
        K += 1
