import sys
from itertools import permutations


def read():
    return sys.stdin.readline().strip()


def get_operators(C):
    operators = ["+", "-", "*", "/"]
    lst_operators = []
    for cnt, operator in zip(C, operators):
        for _ in range(len(cnt)):
            lst_operators.extend(operator)

    return lst_operators


def calculate(A, operator):
    res = A[0]
    for num, entity in zip(A[1:], operator):
        res = int(eval(f"{res}{entity}{num}"))

    return res


if __name__ == "__main__":
    N = int(read())
    A = list(map(int, read().strip().split()))
    C = list([0] * itr for itr in map(int, read().strip().split()))

    result_cal = [
        calculate(A, operator) for operator in set(permutations(get_operators(C)))
    ]
    print(max(result_cal))
    print(min(result_cal))
