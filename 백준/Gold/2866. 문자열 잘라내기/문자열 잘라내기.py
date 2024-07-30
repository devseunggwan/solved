import sys


def read():
    r = sys.stdin.readline

    R, C = map(int, r().strip().split())
    M = [r().strip() for _ in range(R)]
    M = ["".join(x) for x in zip(*M)]

    return R, C, M
    

if __name__ == "__main__":
    R, C, M = read()
    
    counter = 0
    for _ in range(R-1):
        M = [x[1:] for x in M]
        if len(set(M)) == C:
            counter += 1
    
    print(counter)