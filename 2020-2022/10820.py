import sys

while True:
    S = sys.stdin.readline().rstrip('\n')
    if not S: break
    ans = [0 for i in range(4)]

    for s in S:
        if(s.isdigit()): ans[2] += 1
        elif(s.islower()): ans[0] += 1
        elif(s.isupper()): ans[1] += 1
        elif(s == " "): ans[3] += 1
    
    print(*ans)