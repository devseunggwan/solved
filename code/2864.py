A, B = input().strip().split()
V, W, X, Y = "", "", "", ""
for i in A:
    if(i == "5"):
        V += "5"
        W += "6"
    elif(i == "6"):
        V += "5"
        W += "6"
    else:
        V += i
        W += i

for j in B:
    if(j == "5"):
        X += "5"
        Y += "6"
    elif(j == "6"):
        X += "5"
        Y += "6"
    else:
        X += j
        Y += j

print("{} {}".format(int(V)+int(X), int(W)+int(Y)))
