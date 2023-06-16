from collections import deque

N = int(input())
A, B = deque(map(int, input().strip().split())), deque(map(int, input().strip().split()))
win, ans, tmp = False, 0, 1
def fight(a, b):
    global win, ans, tmp, A, B
    if(a == b):
        if(win): B.popleft()
        else: A.popleft()
        win = not win
        tmp = 1
        
    elif(a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b == 1):
        if(not win): 
            win = True
            tmp = 1
        else: tmp +=1
        if(ans < tmp): ans = tmp
        A.popleft()

    elif(a == 2 and b == 1 or a == 3 and b == 2 or a == 1 and b == 3):
        if(win): 
            win = False
            tmp = 1
        else:
            tmp += 1
        if(ans < tmp): ans = tmp
        B.popleft()


while(list(A) and list(B)):
    fight(A[0], B[0])

print(ans-1)