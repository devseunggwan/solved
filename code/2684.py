for T in range(int(input())):
    P = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    C = input()

    for i in range(len(C)-2):
        P[C[i:i+3]] += 1
    
    print(*P.values())