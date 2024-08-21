import sys
from collections import Counter


def read():
    input = sys.stdin.readline
    cases = []

    while True:
        case = (input().strip(), input().strip())

        if case == ("END", "END"):
            break

        cases.append(case)

    return cases


def is_same(A, B):
    return Counter(A) == Counter(B)


if __name__ == "__main__":
    cases = read()

    for idx, case in enumerate(cases):
        print(f"Case {idx+1}: {'same' if is_same(*case) else 'different'}")
