import sys

def readline():
    return sys.stdin.readline()

def get_min_max(lands, N, M):
    __min, __max = 0, 0
        
    for x in range(N):
        for y in range(M):
            if lands[x][y] >= h:
                __max += lands[x][y] - h
            else:
                __min += h - lands[x][y]

    return __min, __max


if __name__ == "__main__":
    N, M, B = map(int, readline().split())
    lands = [list(map(int, readline().split())) for _ in range(N)]
    time, height = sys.maxsize, 0
    
    for h in range(257):
        __min, __max = get_min_max(lands, N, M)
        if __max + B >= __min and __min + (__max * 2) <= time:
            time, height = __min + (__max * 2), h
    
    print(time, height)
