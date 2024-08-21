import sys


def read():
    r = sys.stdin.readline

    T = int(r())
    TC = sorted([int(r()) - 1 for _ in range(T)])

    return T, TC


def get_super_primes():
    primes = []
    M = [1 for _ in range(1000001)]
    M[0], M[1] = 0, 0

    for i in range(2, 1000):
        if M[i]:
            for j in range(i * i, 1000001, i):
                M[j] = 0

    idx = 0
    for i in range(1000001):
        if M[i]:
            idx += 1

            if M[idx]:
                primes.append(i)

    return primes


if __name__ == "__main__":
    T, TC = read()
    primes = get_super_primes()
    for case in TC:
        print(primes[case])
