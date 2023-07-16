while True:
    line = input()
    if line == "0 0":
        break
        
    print(sum(map(int, line.split())))