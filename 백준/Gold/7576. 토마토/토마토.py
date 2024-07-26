import sys
from collections import deque


def read_data():
    r = sys.stdin.readline

    m, n = map(int, r().strip().split())
    box = [list(map(int, r().strip().split())) for _ in range(n)]

    return m, n, box


def is_empty(box):
    for row in box:
        if 0 in row:
            return True

    return False


def main(m, n, box):
    LOCATE = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    queue = deque()
    max_day = 0

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j, 1))

    while queue:
        i, j, day = queue.popleft()

        for x, y in LOCATE:
            if (0 <= i + y < n) and (0 <= j + x < m) and (box[i + y][j + x] == 0):
                box[i + y][j + x] = day + 1
                queue.append((i + y, j + x, day + 1))
                max_day = max(max_day, day)

    empty = is_empty(box)

    return -1 if empty else max_day


if __name__ == "__main__":
    m, n, box = read_data()
    result = main(m, n, box)
    print(result)
