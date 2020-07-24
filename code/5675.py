import sys

while True:
    try:
        r = sys.stdin.readline()
        if(int(r.strip())%6 != 0): print("N")
        else: print("Y")
    except:
        break