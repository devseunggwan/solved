import sys
from itertools import permutations

for i in range(1, int(sys.stdin.readline()) + 1):
    N = int(sys.stdin.readline())
    lst_blocks = str(sys.stdin.readline()).strip().split()

    for blocks in permutations(lst_blocks):
        lst_alpha = [0] * 26
        last_alpha = ""
        IMPOSSIBLE = 0
        for alpha in "".join(blocks):
            if lst_alpha[ord(alpha) - 65] and last_alpha != alpha:
                IMPOSSIBLE = 1
                break
            else:
                lst_alpha[ord(alpha) - 65] += 1
                last_alpha = alpha

        if IMPOSSIBLE:
            continue

        break

    if IMPOSSIBLE:
        print("CASE #{}: IMPOSSIBLE".format(i))
    else:
        print("CASE #{}: {}".format(i, "".join(blocks)))
