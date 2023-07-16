while True:
    line = input()
    if line == "# 0 0":
        break
    
    name, age, weight = line.strip().split()
    stage = "Senior" if int(age) > 17 or int(weight) >= 80 else "Junior"
    print(f"{name} {stage}")