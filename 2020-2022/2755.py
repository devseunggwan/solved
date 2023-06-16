G = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7, 
    "B+": 3.3, "B0": 3.0, "B-": 2.7, 
    "C+": 2.3, "C0": 2.0, "C-": 1.7, 
    "D+": 1.3, "D0": 1.0, "D-": 0.7, 
    "F": 0.0
}

P, H = 0, 0

for T in range(int(input())):
    M = input().strip().split()
    P += int(M[1]) * G[M[2]]
    H += int(M[1])


print("{:.02f}".format(round(P/H + (0.001 if(P/H*100%10) >- 5 else 0), 2)))