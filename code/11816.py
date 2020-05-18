X = input()
if('x' in X):
    print(int(X, 16))
elif(X[0] == "0"):
    print(int("0o{}".format(X[1:]), 8))
else:
    print(X)
