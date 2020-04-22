for i in range(int(input())):
    N, M = map(int, input().strip().split())
    D = [[j, i] for i, j in enumerate(list(map(int, input().strip().split())))]

    print(max(D))
