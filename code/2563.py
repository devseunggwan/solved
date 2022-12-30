import sys


def read():
    return sys.stdin.readline().strip()


lst_whitespace = [[0] * 100 for i in range(100)]
lst_area = [list(map(int, read().strip().split())) for _ in range(int(read()))]

for start_x, start_y in lst_area:
    for y in range(start_y, start_y + 10):
        for x in range(start_x, start_x + 10):
            lst_whitespace[y][x] = 1 if lst_whitespace[y][x] == 0 else 1

res = sum([sum(x) for x in lst_whitespace])
print(res)
