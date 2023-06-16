ball = 1

for i in range(int(input())):
    B = [i for i in map(int, input().strip().split())]
    if(ball in B):
        for j in B:
            if(j != ball): 
                ball = j
                break
            
print(ball)