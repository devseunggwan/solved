B = False
ans = 0
for i in range(8):
    B = not B
    for M in input():
        if(B and M == "F"):
            ans += 1
        B = not B
print(ans)
