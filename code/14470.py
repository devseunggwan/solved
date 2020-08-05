M = [int(input()) for i in range(5)]
ans, c = 0, 1 if M[0] > 0 else 0

while M[0] != M[1]:
    if(M[0] < 0):
        M[0] += 1
        ans += M[2]
    elif(M[0] == 0 and c == 0):
        ans += M[3]
        c += 1
    else:
        ans += M[4]
        M[0] += 1
print(ans)