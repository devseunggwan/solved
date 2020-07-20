from collections import Counter

while True:
    N, T = input().strip(), ""
    if(N == "*"): break
    for i in N.strip().split(): T += i
    if(len(list(Counter(T).values())) != 26): print("N")
    else: print("Y")




