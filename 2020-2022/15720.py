B, C, D = map(int, input().strip().split())
Bur = sorted(map(int, input().strip().split()), reverse=True)
Sid = sorted(map(int, input().strip().split()), reverse=True)
Sod = sorted(map(int, input().strip().split()), reverse=True)
Bef, Aft = 0, 0
ran = min(B, C, D)
for i in range(ran):
    Aft += (Bur[i]+Sid[i]+Sod[i])*0.9

print(sum(Bur) + sum(Sid) + sum(Sod))
print(int(Aft) + sum(Bur[ran:]) + sum(Sid[ran:]) + sum(Sod[ran:]))