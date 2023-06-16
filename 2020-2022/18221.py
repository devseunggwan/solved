import sys
for i in range(int(input())):
    if(int(sys.stdin.readline().strip()) % 2 == 0):
        print("O")
    else:
        print("E")
