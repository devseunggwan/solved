D = {
    "111111": "0",
    "1010": "1",
    "1011101": "2",
    "1001111": "3",
    "1101010": "4",
    "1100111": "5",
    "1110111": "6",
    "1011": "7",
    "1111111": "8",
    "1101011": "9"
}

for V in range(len(D)):
    D[D[list(D.keys())[V]]] = list(D.keys())[V]


while True:
    T = input()
    if(T == "BYE"): break

    A, B = T[:-1].split("+")
    num = ["", ""]
    for i in range(0, len(A), 3):
        num[0] += D[bin(int(A[i:i+3]))[2:]]

    for i in range(0, len(B), 3):
        num[1] += D[bin(int(B[i:i+3]))[2:]]
    
    for k in str(sum(map(int, num))):
        T += ("0" * (3 - len(str(int("0b"+D[k], 2))))) + str(int("0b"+D[k], 2))
    print(T)