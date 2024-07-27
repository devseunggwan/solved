import sys


def read():
    r = sys.stdin.readline

    N = int(r())
    P = [list(map(int, r().strip().split())) for _ in range(N)]

    colors = set([x[1] for x in P])

    return N, P, colors


def get_length(P, colors):
    length = 0
    
    dict_colors = {color: [] for color in colors}

    for item in P:
        dict_colors[item[1]].append(item[0])
    
    for color in colors:
        lines = dict_colors[color]

        if len(lines) == 1:
            continue

        lines.sort()
        length += (lines[1] - lines[0]) + abs(lines[-1] - lines[-2]) + sum([min(lines[i+1] - lines[i], abs(lines[i] - lines[i-1])) for i in range(1, len(lines)-1)])

    return length


if __name__ == "__main__":
    N, P, colors = read()
    answer = get_length(P, colors)

    print(answer)
