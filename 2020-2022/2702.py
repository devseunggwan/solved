T = int(input())


def gcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


for i in range(T):
    a, b = map(int, input().strip().split())
    print(int(lcm(a, b)), gcd(a, b))
