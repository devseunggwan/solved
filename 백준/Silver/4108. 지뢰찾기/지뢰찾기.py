import sys


r = sys.stdin.readline


def mine_count(loc: list[int, int], M: list[list[str]], R: int, C: int) -> str:
    i, j = loc
    FIND_LOC = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    if M[j][i] == "*":
        return "*"
    
    mine = 0
    for x, y in FIND_LOC:
        if 0 <= x + i < C and 0 <= y + j < R and M[y+j][x+i] == "*":
            mine += 1
            
    return str(mine)


if __name__ == "__main__":
    while True:
        R, C = map(int, r().strip().split())

        if R + C == 0:
            break

        M = [list(r().strip()) for _ in range(R)]

        for j in range(R):
            line = "".join([mine_count((i, j), M, R, C) for i in range(C)])
            print(line)
