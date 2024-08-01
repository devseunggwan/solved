from itertools import permutations


def read():
    data = []

    for _ in range(2):
        data.extend(input().strip().split())

    data = list(set(data)) * 2
    data = list(set(permutations(data, r=2)))
    data = sorted(data, key=lambda x: (x[0], x[1]))

    return data


if __name__ == "__main__":
    data = read()

    for item in data:
        print(" ".join(item))
