import sys

def read():
    input = sys.stdin.readline
    
    T = []
    
    while True:
        n = float(input().strip())
        if n == 999.0:
            break
        
        T.append(n)
    
    return T

if __name__ == "__main__":
    T = read()
    
    for i in range(1, len(T)):
        print("%.2f" % (T[i] - T[i - 1]))
