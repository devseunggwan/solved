m = [0, 0, 0, 0, 0]

for idx in range(int(input())):
    x, y = map(int, input().split())
    
    if x > 0 and y > 0:
        m[0] += 1
    elif x < 0 and y > 0:
        m[1] += 1
    elif x < 0 and y < 0:
        m[2] += 1
    elif x > 0 and y < 0:
        m[3] += 1
    else:
        m[4] += 1
        

for i in range(4):
    print(f"Q{i+1}: {m[i]}")

print(f"AXIS: {m[4]}")