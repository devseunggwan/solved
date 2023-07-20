while True:
    res = 1

    tree = list(map(int, input().strip().split()))
    if tree == [0]:
        break

    for idx in range(1, tree[0] * 2, 2):
        res = (res * tree[idx]) - tree[idx+1]

    print(res)