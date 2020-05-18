N = int(input())
P = sorted(map(int, input().split()))
M = int(input())
Q = map(int, input().split())

for i in Q:
    P_s, P_e = 0, len(P)
    while True:
        if(P[(P_s + P_e)//2] < i):
            P_s = P_e//2
        elif(P[(P_s + P_e)//2] > i):
            P_e = (P_s + P_e)//2
        elif(P_):
