while True:
    N = input()

    if N == "0":
        break

    num_space = {
        "0": 4,
        "1": 2,
    }

    space = len(N) + 1
    for i in N:
        if i in num_space.keys():
            space += num_space[i]
        else:
            space += 3

    print(space)
