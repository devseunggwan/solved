import sys


def read():
    return sys.stdin.readline().strip()


def get_lst_counter():
    lst_counter = [0] * 10001
    for _ in range(int(read())):
        lst_counter[int(read())] += 1

    return lst_counter


if __name__ == "__main__":
    lst_counter = get_lst_counter()
    for itr, count in enumerate(lst_counter):
        [print(itr) for _ in range(count)]

# 이렇게 풀면 시간초과
# [print(i) for i in sorted([int(read()) for _ in range(int(read()))])]
