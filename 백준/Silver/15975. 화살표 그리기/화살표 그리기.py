import sys


def read():
    r = sys.stdin.readline

    N = int(r())
    P = [list(map(int, r().strip().split())) for _ in range(N)]

    colors = set([x[1] for x in P])

    return N, P, colors


if __name__ == "__main__":
    N, P, colors = read()
    answer = 0

    for color in colors:
        lines = [x[0] for x in P if x[1] == color]
        lines = sorted(lines)

        if len(lines) == 1:
            continue

        for i in range(len(lines)):
            if i == 0:
                answer += lines[i+1] - lines[i]
            elif i == len(lines) - 1:
                answer += abs(lines[i] - lines[i-1])
            else:
                answer += min(lines[i+1] - lines[i], abs(lines[i] - lines[i-1]))

    print(answer)
