import sys

r = sys.stdin.readline
N, M = map(int, r().strip().split())
orders = []


def order_sort(orders: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(orders, key=lambda x: (x[1], x[0]))


if __name__ == "__main__":

    for _ in range(N):
        a = r().strip().split()

        if a[0] == "order":
            orders.append(tuple(map(int, (a[1], a[2]))))
        elif a[0] == "sort":
            orders = order_sort(orders)
        elif a[0] == "complete":
            for i in range(len(orders)):
                if orders[i][0] == int(a[1]):
                    orders.pop(i)
                    break

        print(" ".join([str(x[0]) for x in orders]) if orders else "sleep")
