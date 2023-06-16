from collections import Counter

for _ in range(int(input())):
    S = input()
    C = Counter(S)


    if(len(S) != 7 or len(C.keys()) != 2): print(0)
    elif(S[0] == S[1] == S[4] and S[2] == S[3] == S[5] == S[6]): print(1)
    else: print(0)
