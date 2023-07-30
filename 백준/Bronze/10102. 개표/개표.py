V, T = int(input()), input()
A, B = 0, 0

for t in T:
    if t == "A":
        A += 1
    else:
        B += 1

if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")