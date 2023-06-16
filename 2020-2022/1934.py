T = int(input())


def lcm(A, B):
    a, b = A, B
    while b != 0:
        a, b = b, a % b
    return (A * B) // a


for _ in range(T):
    A, B = map(int, input().strip().split())
    print(lcm(A, B))
