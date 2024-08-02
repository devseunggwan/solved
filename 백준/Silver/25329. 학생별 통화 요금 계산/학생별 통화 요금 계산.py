import sys
from collections import defaultdict


def read():
    r = sys.stdin.readline

    n = int(r())
    m = [r().strip().split() for _ in range(n)]

    return n, m


def cal_cell_time(cell_time: str):
    hour, second = map(int, cell_time.split(":"))

    return hour * 60 + second


def cal_cell_fee(cell_time: int):
    cell_time, fee = cell_time - 100, 10

    if cell_time <= 0:
        return fee

    cell_time, fee = cell_time % 50, fee + (cell_time // 50) * 3

    if cell_time > 0:
        fee += 3

    return fee


if __name__ == "__main__":
    n, m = read()

    t = defaultdict(int)

    for cell_time, name in m:
        t[name] += cal_cell_time(cell_time)

    v = [(name, cal_cell_fee(cell_time)) for name, cell_time in t.items()]
    v = sorted(v, key=lambda x: (-x[1], x[0]))

    for i in v:
        print(f"{i[0]} {i[1]}")
