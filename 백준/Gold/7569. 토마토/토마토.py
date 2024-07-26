# https://www.acmicpc.net/problem/7569

import sys
from collections import deque


def read_data():
    r = sys.stdin.readline

    m, n, h = map(int, r().strip().split())
    box = [[list(map(int, r().strip().split())) for _ in range(n)] for _ in range(h)]

    return m, n, h, box


def is_empty(boxs):
    for box in boxs:
        for row in box:
            if 0 in row:
                return True

    return False


def main(m, n, h, box):
    LOCATE = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

    queue = deque()
    max_day = 0

    for k in range(h):
        for j in range(n):
            for i in range(m):
                if box[k][j][i] == 1:
                    queue.append((i, j, k, 1))

    while queue:
        i, j, k, day = queue.popleft()

        for x, y, z in LOCATE:
            if (
                (0 <= i + x < m)
                and (0 <= j + y < n)
                and (0 <= k + z < h)
                and (box[k + z][j + y][i + x] == 0)
            ):
                box[k + z][j + y][i + x] = day + 1
                queue.append((i + x, j + y, k + z, day + 1))
                max_day = max(max_day, day)

    empty = is_empty(box)

    return -1 if empty else max_day


if __name__ == "__main__":
    m, n, h, box = read_data()
    result = main(m, n, h, box)
    print(result)
